import confidential
from unsync import unsync
import urllib3
import itertools
import moon

@unsync(cpu_bound=True)
def is_content(x):
    payload = ''.join(x)
    test_url = confidential.preamble + payload
    trial_request = None
    # payload is the thing to stick at the end of the domain you want to test
    # test_url is the whole url
    # initializign trial_request to none, so if it gets changed later, means 
    # there is results

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
        return (test_url, trial_request.status)
    
    else:
        return None


    
http = urllib3.PoolManager(timeout=30,
retries=urllib3.Retry(3, raise_on_redirect=False))

for i in range(128):
    print(f'working on range: {i}')
    search_tator =itertools.combinations_with_replacement(moon.search_space, i)

    good_urls = [is_content(url) for url in search_tator if url]

    for url in good_urls:
        blarga = url.result()

        if blarga:
            print(blarga)