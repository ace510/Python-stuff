from __future__ import print_function
import moon
import confidential
from multiprocessing import Pool
import itertools
import requests

def is_content(x):
    payload = ''.join(x)
    test_url = confidential.preamble + payload
    try:
        trial_request = requests.get(test_url)
    except (ConnectionResetError, requests.exceptions.ChunkedEncodingError):
        return (False, test_url)
    # this is where the request is made, is parallelized!
    if trial_request.status_code not in (404,400,403, 504):
        # this is a list of 'bad' status codes
        # so far 404 is generic URL not found
        # 400 is something that should trigger an internal app but doesn't
        # 403 is  file denied access
        # 504 is a weird bug, maybe rate limiting?
        print(test_url+' returned status code ' + trial_request.status_code)
        # discovering new and exciting Status_codes
        return (True, test_url)
    else:
        return (False, test_url)

if __name__ == "__main__":    
    p = Pool(processes = 50)
    output_set= set()
    task_number = 0
            
    for i in range(1,128):
        for returned_data in p.imap_unordered(is_content, itertools.permutations(moon.search_space, i)):
            if returned_data[0]:
                output_set.add(returned_data[1])
            # elif task_number >= 100:
            #     print(f'DEBUG: input was {returned_data[1]}')
            #     task_number = 0
            # else:
            #     task_number += 1
        
        print('done with search space '+str(i))
        
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