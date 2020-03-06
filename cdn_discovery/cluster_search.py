import gevent
from gevent import monkey; monkey.patch_socket(); monkey.patch_ssl()
from gevent.pool import Group
from gevent import Timeout
import multiprocessing
import multiprocessing.pool
import moon
import itertools
import confidential
# import requests
import urllib3

class NoDaemonProcess(multiprocessing.Process):
    @property
    def daemon(self):
        return False

    @daemon.setter
    def daemon(self, value):
        pass

class NoDaemonContext(type(multiprocessing.get_context())):
    Process = NoDaemonProcess

class UrTooSlow(Exception):
    print('Gotta go fast, n eat chilli dawgs')

# We sub-class multiprocessing.pool.Pool instead of multiprocessing.Pool
# because the latter is only a wrapper function, not a proper class.
class MyPool(multiprocessing.pool.Pool):
    def __init__(self, *args, **kwargs):
        kwargs['context'] = NoDaemonContext()
        super(MyPool, self).__init__(*args, **kwargs)


def iterator_ception():
    for i in range(0,128):
        yield itertools.permutations(moon.search_space, i)


def tater_masher(iter_tater):
    p = Group()
    output_set= set()

    for returned_data in p.imap_unordered(urllib_iscontent, iter_tater, maxsize = 10 ):
        # if len(p) <= 5:
        #     print(f'there are only {len(p)} waiting')
        if returned_data[0]:
            output_set.add(returned_data[1])
            print(f'the list of data i\'m going to return is {len(output_set)}')
    
    return output_set



 
def sonuva_iscontent(request_string):
    payload = ''.join(request_string)
    test_url = confidential.preamble + payload
    trial_request = None
    
    try:
        # with Timeout(180, UrTooSlow):
        trial_request = requests.get(test_url)
    except (requests.exceptions.ConnectionError): 
        # OSError is too broad, fishing for  WindowsError()
        return (False, test_url)
    except requests.exceptions.ChunkedEncodingError:
        print('how many times do we have to teach you this old man?')
    except OSError(420):
        print('big fat cero')
        return (False, test_url)
    except UrTooSlow:
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
    elif trial_request.status_code in (403, 504, 500, 503):
        print(f'{test_url} failed with {trial_request.status_code}')
        return (False, test_url)
    else:
        return (False, test_url)

def urllib_iscontent(request_string):
    payload = ''.join(request_string)
    test_url = confidential.preamble + payload
    trial_request = None
    http = urllib3.PoolManager(maxsize=10, timeout=180,
    retries=urllib3.Retry(3, raise_on_redirect=False))

    try:
        trial_request = http.request('GET', test_url)
    except OSError:
        print('URLLIB error, halp')
        return (False, test_url)
    
    if trial_request is None:
        return (False, test_url)
    
    if trial_request.status not in (404,400,403, 504, 500):
        print(f'{test_url} returned status code {trial_request.status}')
        return (True, test_url)
    elif trial_request.status in (403, 504, 500, 503):
        print(f'{test_url} failed with {trial_request.status}')
        return (False, test_url)
    else:
        return(False, test_url)

def main():
    process_count = 2
    # start_length = 0
    print('Hello world')
    Fought_the_law = iterator_ception()
    print('iterator up')
    p = MyPool(process_count)
    print('pool going')

    
    print('set engaged')

    for returned_stuff in p.imap_unordered(tater_masher,Fought_the_law):
        outputsquared_set = set()
        for _ in returned_stuff:
            print(f'egads, I found a {returned_stuff}')
            outputsquared_set.add(returned_stuff)
        print('will this print?')
        with open('results_saver.txt','a') as file:
            for item in outputsquared_set:
                file.write(item)

    print('this will not print in the heatdeath of the universe')
    print('so how are you doing, weary time traveler?')
    print('pull up a chair, watch the stars die')



if __name__ == "__main__":
    main()