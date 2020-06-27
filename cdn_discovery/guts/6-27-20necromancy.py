import gevent
from gevent import monkey; monkey.patch_socket(); monkey.patch_ssl()
import multiprocessing
import multiprocessing.pool
import confidential
import moon
from gevent.pool import Pool
from gevent.pool import Group
import itertools
import urllib3
import time

class NoDaemonProcess(multiprocessing.Process):
    @property
    def daemon(self):
        return False

    @daemon.setter
    def daemon(self, value):
        pass


class NoDaemonContext(type(multiprocessing.get_context())):
    Process = NoDaemonProcess

# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class MyPool(multiprocessing.pool.Pool):
    def __init__(self, *args, **kwargs):
        kwargs['context'] = NoDaemonContext()
        super(MyPool, self).__init__(*args, **kwargs)

def searcher(length):
    p = Group()
    http = urllib3.PoolManager(num_pools = 100, timeout=180,
    retries=urllib3.Retry(3, raise_on_redirect=False))


    for returned_data in p.imap_unordered(is_content, 
        itertools.combinations_with_replacement(moon.search_space, length), 
        maxsize =  10):
            if returned_data[0]:
                return returned_data

def is_content(x):
    http = urllib3.PoolManager(num_pools = 100, timeout=180,
    retries=urllib3.Retry(3, raise_on_redirect=False))

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
    process_count = 4
    # start_length = 0
    http = urllib3.PoolManager(num_pools = 100, timeout=180,
    retries=urllib3.Retry(3, raise_on_redirect=False))

    print('Hello world')

    print('iterator up')
    p = MyPool(4)
    print('pool going')

    for returned_stuff in p.imap_unordered(searcher,range(128)):
        outputsquared_set = set()
        if returned_stuff:
            for _ in returned_stuff:
                print(f'egads, I found a {returned_stuff}')
                outputsquared_set.add(returned_stuff)
            print('will this print?')
        with open('results_saver.txt','a') as file:
            for item in outputsquared_set:
                file.write(item)    