"""
This type stub file was generated by pyright.
"""

import re
from collections import namedtuple

url_attrs = ["scheme", "auth", "host", "port", "path", "query", "fragment"]
NORMALIZABLE_SCHEMES = ("http", "https", None)
PERCENT_RE = re.compile(r"%[a-fA-F0-9]{2}")
SCHEME_RE = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+-]*:|/)")
URI_RE = re.compile(r"^(?:([a-zA-Z][a-zA-Z0-9+.-]*):)?" r"(?://([^/?#]*))?" r"([^?#]*)" r"(?:\?([^#]*))?" r"(?:#(.*))?$", re.UNICODE | re.DOTALL)
IPV4_PAT = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
HEX_PAT = "[0-9A-Fa-f]{1,4}"
LS32_PAT = "(?:{hex}:{hex}|{ipv4})".format(hex=HEX_PAT, ipv4=IPV4_PAT)
_subs = { "hex": HEX_PAT,"ls32": LS32_PAT }
_variations = ["(?:%(hex)s:){6}%(ls32)s", "::(?:%(hex)s:){5}%(ls32)s", "(?:%(hex)s)?::(?:%(hex)s:){4}%(ls32)s", "(?:(?:%(hex)s:)?%(hex)s)?::(?:%(hex)s:){3}%(ls32)s", "(?:(?:%(hex)s:){0,2}%(hex)s)?::(?:%(hex)s:){2}%(ls32)s", "(?:(?:%(hex)s:){0,3}%(hex)s)?::%(hex)s:%(ls32)s", "(?:(?:%(hex)s:){0,4}%(hex)s)?::%(ls32)s", "(?:(?:%(hex)s:){0,5}%(hex)s)?::%(hex)s", "(?:(?:%(hex)s:){0,6}%(hex)s)?::"]
UNRESERVED_PAT = r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._!\-~"
IPV6_PAT = "(?:" + "|".join([x % _subs for x in _variations]) + ")"
ZONE_ID_PAT = "(?:%25|%)(?:[" + UNRESERVED_PAT + "]|%[a-fA-F0-9]{2})+"
IPV6_ADDRZ_PAT = r"\[" + IPV6_PAT + r"(?:" + ZONE_ID_PAT + r")?\]"
REG_NAME_PAT = r"(?:[^\[\]%:/?#]|%[a-fA-F0-9]{2})*"
TARGET_RE = re.compile(r"^(/[^?#]*)(?:\?([^#]*))?(?:#.*)?$")
IPV4_RE = re.compile("^" + IPV4_PAT + "$")
IPV6_RE = re.compile("^" + IPV6_PAT + "$")
IPV6_ADDRZ_RE = re.compile("^" + IPV6_ADDRZ_PAT + "$")
BRACELESS_IPV6_ADDRZ_RE = re.compile("^" + IPV6_ADDRZ_PAT[2: - 2] + "$")
ZONE_ID_RE = re.compile("(" + ZONE_ID_PAT + r")\]$")
SUBAUTHORITY_PAT = u"^(?:(.*)@)?(%s|%s|%s)(?::([0-9]{0,5}))?$" % (REG_NAME_PAT, IPV4_PAT, IPV6_ADDRZ_PAT)
SUBAUTHORITY_RE = re.compile(SUBAUTHORITY_PAT, re.UNICODE | re.DOTALL)
UNRESERVED_CHARS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-~")
SUB_DELIM_CHARS = set("!$&'()*+,;=")
USERINFO_CHARS = UNRESERVED_CHARS | SUB_DELIM_CHARS | ":"
PATH_CHARS = USERINFO_CHARS | "@", "/"
QUERY_CHARS = FRAGMENT_CHARS = PATH_CHARS | "?"
class Url(namedtuple("Url", url_attrs)):
    """
    Data structure for representing an HTTP URL. Used as a return value for
    :func:`parse_url`. Both the scheme and host are normalized as they are
    both case-insensitive according to RFC 3986.
    """
    __slots__ = ...
    def __new__(cls, scheme=..., auth=..., host=..., port=..., path=..., query=..., fragment=...):
        ...
    
    @property
    def hostname(self):
        """For backwards-compatibility with urlparse. We're nice like that."""
        ...
    
    @property
    def request_uri(self):
        """Absolute path including the query string."""
        ...
    
    @property
    def netloc(self):
        """Network location including host and port"""
        ...
    
    @property
    def url(self):
        """
        Convert self into a url

        This function should more or less round-trip with :func:`.parse_url`. The
        returned url may not be exactly the same as the url inputted to
        :func:`.parse_url`, but it should be equivalent by the RFC (e.g., urls
        with a blank port will have : removed).

        Example: ::

            >>> U = parse_url('http://google.com/mail/')
            >>> U.url
            'http://google.com/mail/'
            >>> Url('http', 'username:password', 'host.com', 80,
            ... '/path', 'query', 'fragment').url
            'http://username:password@host.com:80/path?query#fragment'
        """
        ...
    
    def __str__(self) -> str:
        ...
    


def split_first(s, delims):
    """
    .. deprecated:: 1.25

    Given a string and an iterable of delimiters, split on the first found
    delimiter. Return two split parts and the matched delimiter.

    If not found, then the first part is the full input string.

    Example::

        >>> split_first('foo/bar?baz', '?/=')
        ('foo', 'bar?baz', '/')
        >>> split_first('foo/bar?baz', '123')
        ('foo/bar?baz', '', None)

    Scales linearly with number of delims. Not ideal for large number of delims.
    """
    ...

def parse_url(url):
    """
    Given a url, return a parsed :class:`.Url` namedtuple. Best-effort is
    performed to parse incomplete urls. Fields not provided will be None.
    This parser is RFC 3986 compliant.

    The parser logic and helper functions are based heavily on
    work done in the ``rfc3986`` module.

    :param str url: URL to parse into a :class:`.Url` namedtuple.

    Partly backwards-compatible with :mod:`urlparse`.

    Example::

        >>> parse_url('http://google.com/mail/')
        Url(scheme='http', host='google.com', port=None, path='/mail/', ...)
        >>> parse_url('google.com:80')
        Url(scheme=None, host='google.com', port=80, path=None, ...)
        >>> parse_url('/foo?bar')
        Url(scheme=None, host=None, port=None, path='/foo', query='bar', ...)
    """
    ...

def get_host(url):
    """
    Deprecated. Use :func:`parse_url` instead.
    """
    ...

