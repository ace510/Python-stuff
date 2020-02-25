import gevent
from gevent import monkey; monkey.patch_all()
import moon
import confidential
from gevent.pool import Pool
import itertools
import requests
import time
from requests.exceptions import ChunkedEncodingError


def is_content(x):
    payload = ''.join(x)
    test_url = confidential.preamble + payload
    trial_request = None
    
    try:
        with gevent.Timeout(180,False):
            trial_request = requests.get(test_url)
    except (ConnectionResetError, ChunkedEncodingError, WindowsError(420) ): 
        # OSError is too broad, fishing for  WindowsError() 
        return (False, test_url)
    except OSError:
        print('big fat cero')
        return (False, test_url)
    except TimeoutError:
        print('help me')
        return (False, test_url)

    if trial_request is None:
        return (False, test_url)
    # except IndexError:
    #     print('wake me up, wake me up inside')
    # this is where the request is made, is parallelized!
    if trial_request.status_code not in (404,400,403, 504, 500):
        # this is a list of 'bad' status codes
        # so far 404 is generic URL not found
        # 400 is something that should trigger an internal app but doesn't
        # 403 is  file denied access
        # 504 is a weird bug, maybe rate limiting?
        print(f'{test_url} returned status code {trial_request.status_code}')
        # discovering new and exciting Status_codes
        return (True, test_url)
    elif trial_request.status_code in (403,504, 500):
        print(f'{test_url} failed with {trial_request.status_code}')
        return (False, test_url)
    else:
        return (False, test_url)

if __name__ == "__main__":    
    p = Pool(250)
    output_set= set()
    task_number = 0
    workers = 0
    start_length = 3

    # changing start_length changes how short the url selector length
    for i in range(start_length,128):
        for returned_data in p.imap_unordered(is_content, itertools.permutations(moon.search_space, i)):
            if returned_data[0]:
                output_set.add(returned_data[1])
            elif (len_p := len(p)) != workers:
                print(f'there are {len_p} workers')
                workers = len_p

            # elif task_number >= 100:
            #      print(f'DEBUG: input was {returned_data[1]}')
            #      task_number = 0
            # else:
            #      task_number += 1
        
        print(f'done with search space {i}')
            # output = results.get()
            # for item in output:
            #     if item != 0:
            #         print(item)
            #         output_set.add(item)
            
    with open('results_mt.md','w') as file:
        for item in output_set:
            file.write(item)
        
        #print(test_url)
        # the postamble will start with a, b, c, d and work out to longer
        # 128 is chosen as a sane upper bound