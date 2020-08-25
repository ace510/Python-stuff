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

PROCS = multiprocessing.cpu_count()

headers = urllib3.make_headers(keep_alive=True, accept_encoding=True)
    
http = urllib3.PoolManager(timeout=30, headers=headers,
retries=urllib3.Retry(3, raise_on_redirect=False))

url_tator = URL_iterator()

task_queue =multiprocessing.Queue(maxsize=PROCS*2)

while True:
    while task_queue.qsize < PROCS:
        task_queue.put([next(url_tator)])


