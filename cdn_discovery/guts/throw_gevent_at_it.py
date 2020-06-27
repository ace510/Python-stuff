import gevent
from gevent import monkey; monkey.patch_all()
import confidential
import moon
from gevent.pool import Pool
from gevent.pool import Group
import itertools
# import requests
import urllib3
import time
from requests.exceptions import ConnectionError

def time_stamp():
    the_now = time.localtime()
    if the_now.tm_hour == 0:
        fixed_hour = 12
    else:
        fixed_hour = the_now.tm_hour
    
    if the_now.tm_min in range(10):
        fixed_min = '0' + str(the_now.tm_min)
    else:
        fixed_min = the_now.tm_min


    stam_parts = (f'{the_now.tm_mon}/{the_now.tm_mday} {fixed_hour}:'
    f'{fixed_min}~')

    return stam_parts


def is_content(x):
    payload = ''.join(x)
    test_url = confidential.preamble + payload
    trial_request = None
    # payload is the thing to stick at the end of the domain you want to test
    # test_url is the whole url
    # initializing trial_request to none, so if it gets changed later, means 
    # there is results

    try:
        # with gevent.Timeout(180,TimeoutError):
        trial_request = http.request('GET', test_url)
    # make request, with 3 minute timeout, urllib seems more efficient than 
    # requests for my needs
    # 1 AM Ian: why timeout? but the script is running stably, no reason to
    # touchy touchy
    except TimeoutError:
        print('help me')
        return (False, test_url)
    except urllib3.exceptions.MaxRetryError:
        print('whoops that request failed')
        return (False, test_url)
    # catch timeout exception, return no data
    if trial_request is None:
        return (False, test_url)
    



    if trial_request.status not in (404,400,403, 504, 500, 502, 503):
        # this is a list of 'bad' status codes
        # so far 404 is generic URL not found
        # 400 is something that should trigger an internal app but doesn't
        # 403 is  file denied access
        # 504 is a weird bug, maybe rate limiting?
        # 502 is bad gateway
        # 503 means service is overloaded or unavailable
        print(f'{time_stamp()}{payload} returned status code '
        f'{trial_request.status}')

        # discovering new and exciting Status_codes
        return (True, test_url)
    elif trial_request.status in (504, 500, 502, 503):
        print(f'{time_stamp()}{payload} failed with {trial_request.status}')
        return (False, test_url)
    else:
        return (False, test_url)

if __name__ == "__main__":

    with open('results_mt.md','w') as file:
        file.write(f'run starting at {time_stamp()}')


    # p = Pool(250)
    # dis worked
    p = Group()
    output_set= set()
    task_number = 0
    workers = 0
    run_time = 0
    notify_minutes = 5
    notify = notify_minutes * 60
    # see note explaining 4 start_length
    start_length = 0
    # nothing interesting came from a payload less than 3 digits
    # search length 3 can be done in 10 minutes, shows nothing

    http = urllib3.PoolManager(num_pools = 100, timeout=180,
    retries=urllib3.Retry(3, raise_on_redirect=False))

    # changing start_length changes how short the url selector length starts off
    for i in range(start_length,4):
        current_time = time.time()
        iter_count = 0

        for returned_data in p.imap_unordered(is_content, 
        itertools.combinations_with_replacement(moon.search_space, i), 
        maxsize =  100):
            iter_count += 1
            if returned_data[0]:
                with open('results_mt.md','a') as file:
                    file.write(returned_data[1])
            
            # if time.time() > (run_time + notify):
            #     print(f'{time_stamp()} testing {returned_data[1]}')
            #     run_time = time.time()
            
        print(f'done with search space {i}')
        elapsed_time = time.time() - current_time
        print(f'took {elapsed_time} seconds')
        print(f'with a total of {iter_count} searches')
        print(f'averaging {elapsed_time / iter_count} per search')

            
        # with open('results_mt.md','w') as file:
        #     for item in output_set:
        #         file.write(item)
            
        #print(test_url)
        # the postamble will start with a, b, c, d and work out to longer
        # 128 is chosen as a sane upper bound
        # in memoriam, I am a dumbass, permutations doesn't repeat selections, 
        # i need combinations with replacement
    
    print('should never print within the heat death of the universe')