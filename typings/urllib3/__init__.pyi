"""
This type stub file was generated by pyright.
"""

import warnings
import logging
from __future__ import absolute_import
from .connectionpool import HTTPConnectionPool, HTTPSConnectionPool, connection_from_url
from . import exceptions
from .filepost import encode_multipart_formdata
from .poolmanager import PoolManager, ProxyManager, proxy_from_url
from .response import HTTPResponse
from .util.request import make_headers
from .util.url import get_host
from .util.timeout import Timeout
from .util.retry import Retry
from logging import NullHandler

"""
urllib3 - Thread-safe connection pooling and re-using.
"""
__author__ = "Andrey Petrov (andrey.petrov@shazow.net)"
__license__ = "MIT"
__version__ = "1.25.8"
def add_stderr_logger(level=...):
    """
    Helper for quickly adding a StreamHandler to the logger. Useful for
    debugging.

    Returns the handler after adding it.
    """
    ...

def disable_warnings(category=...):
    """
    Helper for quickly disabling all urllib3 warnings.
    """
    ...
