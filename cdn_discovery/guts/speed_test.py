import gevent
from gevent import monkey

monkey.patch_all()
import itertools
import urllib3
from gevent.pool import Group
import moon
import confidential
import time


def is_content(x):
    payload = "".join(x)
    test_url = confidential.preamble + payload
    trial_request = None
    # payload is the thing to stick at the end of the domain you want to test
    # test_url is the whole url
    # initializing trial_request to none, so if it gets changed later, means
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


if __name__ == "__main__":
    p = Group()
    http = urllib3.PoolManager(
        timeout=180, retries=urllib3.Retry(3, raise_on_redirect=False)
    )

    current_time = time.time()

    for i in range(3):
        for returned_data in p.imap_unordered(
            is_content,
            itertools.combinations_with_replacement(moon.search_space, i),
            maxsize=10,
        ):

            if returned_data[0]:
                with open("results_mt.md", "a") as file:
                    file.write(returned_data[1])

            if time.time() > (run_time + notify):
                print(f"{time_stamp()} testing {returned_data[1]}")
                run_time = time.time()

        print(f"done with search space {i}")
