import gevent
from gevent import monkey

monkey.patch_all()
import moon
import confidential
from gevent.pool import Pool
from gevent.pool import Group
import itertools

# import requests
import urllib3
import time
from requests.exceptions import ConnectionError

bad_data = (
    b"Access is forbidden\r\n",
    b"<html>\r\n<head><title>400 Bad Request</title></head>\r\n<body>\r\n<cente"
    b"r><h1>400 Bad Request</h1></center>\r\n<hr><center>nginx</center>\r\n</bo"
    b"dy>\r\n</html>\r\n",
)


def time_stamp():
    the_now = time.localtime()
    if the_now.tm_hour == 0:
        fixed_hour = 12
    else:
        fixed_hour = the_now.tm_hour

    if the_now.tm_min in range(10):
        fixed_min = "0" + str(the_now.tm_min)
    else:
        fixed_min = the_now.tm_min

    stam_parts = f"{the_now.tm_mon}/{the_now.tm_mday} {fixed_hour}:" f"{fixed_min}~"

    return stam_parts


def is_content(x):
    payload = "".join(x)
    test_url = confidential.preamble + payload
    trial_request = None
    # payload is the thing to stick at the end of the domain you want to test
    # test_url is the whole url
    # initializign trial_request to none, so if it gets changed later, means
    # there is results

    try:
        # with gevent.Timeout(180,TimeoutError):
        trial_request = http.request("GET", test_url)
    # make request, with 3 minute timeout, urllib seems more efficient than
    # requests for my needs
    # 1 AM Ian: why timeout? but the script is running stably, no reason to
    # touchy touchy
    except TimeoutError:
        print("help me")
        return (False, test_url)
    except urllib3.exceptions.MaxRetryError:
        print("whoops that request failed")
        return (False, test_url)
    # catch timeout exception, return no data
    if trial_request is None:
        return (False, test_url)

    # trial_request

    if trial_request.status not in (404, 400, 403, 504, 500, 502, 503):
        # this is a list of 'bad' status codes
        # so far 404 is generic URL not found
        # 400 is something that should trigger an internal app but doesn't
        # 403 is  file denied access
        # 504 is a weird bug, maybe rate limiting?
        # 502 is bad gateway
        # 503 means service is overloaded or unavailible
        print(
            f"{time_stamp()}{payload} returned status code " f"{trial_request.status}"
        )

        # discovering new and exciting Status_codes
        return (True, test_url)
    elif trial_request.status in (504, 500, 502, 503):
        print(f"{time_stamp()}{payload} failed with {trial_request.status}")
        return (False, test_url, trial_request.data, trial_request.headers)
    else:
        return (False, test_url, trial_request.data, trial_request.headers)


if __name__ == "__main__":

    fancy_dict = {
        "Server": set(),
        "Content": set(),
        "Connection": set(),
        "Content-Type": set(),
        "Cache-Control": set(),
    }

    bad_keys = ("Date", "Content-Length")

    with open("results_mt.md", "a") as file:
        file.write(f"run starting at {time_stamp()}")

    p = Group()
    output_set = set()
    start_length = 1
    run_time = 0
    # nothing interesting came from a payload less than 3 digits

    http = urllib3.PoolManager(
        timeout=180, retries=urllib3.Retry(3, raise_on_redirect=False)
    )

    # changing start_length changes how short the url selector length starts off
    for i in range(start_length, 128):
        for returned_data in p.imap_unordered(
            is_content,
            itertools.combinations_with_replacement(moon.search_space, i),
            maxsize=10,
        ):

            if returned_data[0]:
                with open("results_mt.md", "a") as file:
                    file.write(returned_data[1])
                    file.write("\n")
                    print(returned_data[1])
            else:
                data, headers = returned_data[2:]

            if time.time() > (run_time + 60):
                print(f"{time_stamp()} testing {returned_data[1]}")
                run_time = time.time()

            if data not in bad_data:
                print(f"URL is {returned_data[1]}")
                print(f"Data is: {data} ")
                print(f"Headers is: {headers}")
                print(f"Total Headers is: {fancy_dict}")
                _ = input("continue?")

            for key, value in headers.items():
                if key not in bad_keys:
                    fancy_dict[key].add(value)

        print(f"done with search space {i}")

        # with open('results_mt.md','w') as file:
        #     for item in output_set:
        #         file.write(item)

        # print(test_url)
        # the postamble will start with a, b, c, d and work out to longer
        # 128 is chosen as a sane upper bound
        # in memorium, I am a dumbass, permutations doesn't repeat selections,
        # i need combinations with replacement

    print("should never print within the heat death of the universe")
