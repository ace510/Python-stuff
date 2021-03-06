import confidential
from unsync import unsync
import urllib3
import itertools
import moon
import time
import logging
from datetime import datetime

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, SmallInteger
from sqlalchemy.orm import sessionmaker


logging.basicConfig(
    level=logging.INFO)

def URL_iterator():
    for i in range(0, 128):
        for j in itertools.combinations_with_replacement(moon.search_space, i):
            payload = "".join(j)
            yield "".join((confidential.preamble, payload))
        logging.info(f'done with range {i}')


@unsync
def is_content(test_url):
    trial_request = None
    # payload is the thing to stick at the end of the domain you want to test
    # test_url is the whole url
    # initializing trial_request to none, so if it gets changed later, means
    # there is results

    try:
        trial_request = http.request("GET", test_url)
    # make request, with 3 minute timeout, urllib seems more efficient than
    # requests for my needs
    # 1 AM Ian: why timeout? but the script is running stably, no reason to
    # appeased the 1AM Ian and removed timeout
    except TimeoutError:
        print("help me")
        return None
    except urllib3.exceptions.MaxRetryError:
        print("whoops that request failed")
        return None

    if trial_request.status not in  (404,403): # removed 403, 400, 504, 500, 502, 503
        # this is a list of 'bad' status codes
        # so far 404 is generic URL not found
        # 400 is something that should trigger an internal app but doesn't
        # 403 is  file denied access
        # 504 is a weird bug, maybe rate limiting?
        # 502 is bad gateway
        # 503 means service is overloaded or unavailable
        return (test_url, trial_request.status)

    else:
        return None

engine = create_engine(confidential.db_conf, echo=True)
Base= declarative_base()
Session = sessionmaker(bind=engine)
class URL_info(Base):
    __tablename__ = 'url_info'

    URL_STR = Column(String(200), primary_key=True, unique = True, nullable=False)
    returned_status = Column(SmallInteger, nullable=False)
    time_created = Column(DateTime, nullable=False)

Base.metadata.create_all(engine)


headers = urllib3.make_headers(keep_alive=True, accept_encoding=True)
http = urllib3.PoolManager(
    maxsize = 100,
    block = True,
    timeout=30, headers=headers, retries=urllib3.Retry(3, raise_on_redirect=False)
)

search_tator = URL_iterator()
round_num = 0
proc_time = int(time.time())
batch_size = 10000

logging.info(f'SQLalchemy is currently version {sqlalchemy.__version__}')


while True:
    round_num += 1
    logging.info(f"currently computing round: {round_num}")

    the_now = int(time.time())
    elapsed_time = the_now - proc_time
    logging.info(f'took {elapsed_time} for this batch')
    # logging.info(f"it's taking {elapsed_time/batch_size*1000} ms per operation")
    proc_time = the_now

    good_urls = [is_content(next(search_tator)) for _ in range(batch_size)]
    
    session=Session()
    logging
    for url in good_urls:
        url_result = url.result()
        if url_result:
            new_url = URL_info(URL_STR = url_result[0], returned_status = url_result[1], time_created = datetime.now() )
            session.merge(new_url)
    session.commit()