"""
This type stub file was generated by pyright.
"""

def is_fp_closed(obj):
    """
    Checks whether a given file-like object is closed.

    :param obj:
        The file-like object to check.
    """
    ...

def assert_header_parsing(headers):
    """
    Asserts whether all headers have been successfully parsed.
    Extracts encountered errors from the result of parsing headers.

    Only works on Python 3.

    :param headers: Headers to verify.
    :type headers: `httplib.HTTPMessage`.

    :raises urllib3.exceptions.HeaderParsingError:
        If parsing errors are found.
    """
    ...

def is_response_to_head(response):
    """
    Checks whether the request of a response has been a HEAD-request.
    Handles the quirks of AppEngine.

    :param conn:
    :type conn: :class:`httplib.HTTPResponse`
    """
    ...

