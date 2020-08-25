import confidential
import urllib3
import itertools
import moon
import time
import multiprocessing

def URL_iterator():
    for length in range(0,128):
        for l_sequence in itertools.combinations_with_replacement(
            moon.search_space, length):
            payload = ''.join(l_sequence)
            yield ''.join((confidential.preamble,payload))

def is_content(task_queue,result_queue):

    headers = urllib3.make_headers(keep_alive=True, accept_encoding=True)  
    http = urllib3.PoolManager(timeout=30, headers=headers,
    retries=urllib3.Retry(3, raise_on_redirect=False))
    
    output_set = set()
    chunkus = task_queue.get()

    for test_url in chunkus:

        try:
            trial_request = http.request('GET', test_url)
        # make request, with 3 minute timeout, urllib seems more efficient than 
        # requests for my needs
        # 1 AM Ian: why timeout? but the script is running stably, no reason to
        # appeased the 1AM Ian and removed timeout
        except TimeoutError:
            print('help me')
            return None
        except urllib3.exceptions.MaxRetryError:
            print('whoops that request failed')
            return None

        if trial_request.status not in (404,400,403, 504, 500, 502, 503):
            # this is a list of 'bad' status codes
            # so far 404 is generic URL not found
            # 400 is something that should trigger an internal app but doesn't
            # 403 is  file denied access
            # 504 is a weird bug, maybe rate limiting?
            # 502 is bad gateway
            # 503 means service is overloaded or unavailible
            output_set.add(test_url)
        
        result_queue.put(output_set)


PROCS = multiprocessing.cpu_count()

# headers = urllib3.make_headers(keep_alive=True, accept_encoding=True)  
# http = urllib3.PoolManager(timeout=30, headers=headers,
# retries=urllib3.Retry(3, raise_on_redirect=False))

url_tator = URL_iterator()

task_queue =multiprocessing.Queue(maxsize=PROCS*2)
result_queue =multiprocessing.Queue(maxsize=PROCS)

process_list = []
for proc in range(PROCS):
    p= multiprocessing.Process(target=is_content, args=(task_queue,result_queue,))
    p.start()
    process_list.append(p)


while True:
    while task_queue.qsize() < PROCS:
        task_queue.put([next(url_tator) for i in range(10000)])

    result_cont  = result_queue.get()
    for url in result_cont:
        print(url)


