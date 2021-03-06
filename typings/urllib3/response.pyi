"""
This type stub file was generated by pyright.
"""

import io
import logging

log = logging.getLogger(__name__)
class DeflateDecoder(object):
    def __init__(self) -> None:
        ...
    
    def __getattr__(self, name):
        ...
    
    def decompress(self, data):
        ...
    


class GzipDecoderState(object):
    FIRST_MEMBER = ...
    OTHER_MEMBERS = ...
    SWALLOW_DATA = ...


class GzipDecoder(object):
    def __init__(self) -> None:
        ...
    
    def __getattr__(self, name):
        ...
    
    def decompress(self, data):
        ...
    


if brotli is not None:
    class BrotliDecoder(object):
        def __init__(self) -> None:
            ...
        
        def decompress(self, data):
            ...
        
        def flush(self):
            ...
        
    
    
class MultiDecoder(object):
    """
    From RFC7231:
        If one or more encodings have been applied to a representation, the
        sender that applied the encodings MUST generate a Content-Encoding
        header field that lists the content codings in the order in which
        they were applied.
    """
    def __init__(self, modes) -> None:
        ...
    
    def flush(self):
        ...
    
    def decompress(self, data):
        ...
    


class HTTPResponse(io.IOBase):
    """
    HTTP Response container.

    Backwards-compatible to httplib's HTTPResponse but the response ``body`` is
    loaded and decoded on-demand when the ``data`` property is accessed.  This
    class is also compatible with the Python standard library's :mod:`io`
    module, and can hence be treated as a readable object in the context of that
    framework.

    Extra parameters for behaviour not present in httplib.HTTPResponse:

    :param preload_content:
        If True, the response's body will be preloaded during construction.

    :param decode_content:
        If True, will attempt to decode the body based on the
        'content-encoding' header.

    :param original_response:
        When this HTTPResponse wrapper is generated from an httplib.HTTPResponse
        object, it's convenient to include the original for debug purposes. It's
        otherwise unused.

    :param retries:
        The retries contains the last :class:`~urllib3.util.retry.Retry` that
        was used during the request.

    :param enforce_content_length:
        Enforce content length checking. Body returned by server must match
        value of Content-Length header, if present. Otherwise, raise error.
    """
    CONTENT_DECODERS = ...
    if brotli is not None:
        ...
    REDIRECT_STATUSES = ...
    def __init__(self, body=..., headers=..., status=..., version=..., reason=..., strict=..., preload_content=..., decode_content=..., original_response=..., pool=..., connection=..., msg=..., retries=..., enforce_content_length=..., request_method=..., request_url=..., auto_close=...) -> None:
        ...
    
    def get_redirect_location(self):
        """
        Should we redirect and where to?

        :returns: Truthy redirect location string if we got a redirect status
            code and valid location. ``None`` if redirect status and no
            location. ``False`` if not a redirect status code.
        """
        ...
    
    def release_conn(self):
        ...
    
    @property
    def data(self):
        ...
    
    @property
    def connection(self):
        ...
    
    def isclosed(self):
        ...
    
    def tell(self):
        """
        Obtain the number of bytes pulled over the wire so far. May differ from
        the amount of content returned by :meth:``HTTPResponse.read`` if bytes
        are encoded on the wire (e.g, compressed).
        """
        ...
    
    DECODER_ERROR_CLASSES = ...
    if brotli is not None:
        ...
    def read(self, amt=..., decode_content=..., cache_content=...):
        """
        Similar to :meth:`httplib.HTTPResponse.read`, but with two additional
        parameters: ``decode_content`` and ``cache_content``.

        :param amt:
            How much of the content to read. If specified, caching is skipped
            because it doesn't make sense to cache partial content as the full
            response.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.

        :param cache_content:
            If True, will save the returned data such that the same result is
            returned despite of the state of the underlying file object. This
            is useful if you want the ``.data`` property to continue working
            after having ``.read()`` the file object. (Overridden if ``amt`` is
            set.)
        """
        ...
    
    def stream(self, amt=..., decode_content=...):
        """
        A generator wrapper for the read() method. A call will block until
        ``amt`` bytes have been read from the connection or until the
        connection is closed.

        :param amt:
            How much of the content to read. The generator will return up to
            much data per iteration, but may return less. This is particularly
            likely when using compressed data. However, the empty string will
            never be returned.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        """
        ...
    
    @classmethod
    def from_httplib(ResponseCls, r, **response_kw):
        """
        Given an :class:`httplib.HTTPResponse` instance ``r``, return a
        corresponding :class:`urllib3.response.HTTPResponse` object.

        Remaining parameters are passed to the HTTPResponse constructor, along
        with ``original_response=r``.
        """
        ...
    
    def getheaders(self):
        ...
    
    def getheader(self, name, default=...):
        ...
    
    def info(self):
        ...
    
    def close(self):
        ...
    
    @property
    def closed(self):
        ...
    
    def fileno(self):
        ...
    
    def flush(self):
        ...
    
    def readable(self):
        ...
    
    def readinto(self, b):
        ...
    
    def supports_chunked_reads(self):
        """
        Checks if the underlying file-like object looks like a
        httplib.HTTPResponse object. We do this by testing for the fp
        attribute. If it is present we assume it returns raw chunks as
        processed by read_chunked().
        """
        ...
    
    def read_chunked(self, amt=..., decode_content=...):
        """
        Similar to :meth:`HTTPResponse.read`, but with an additional
        parameter: ``decode_content``.

        :param amt:
            How much of the content to read. If specified, caching is skipped
            because it doesn't make sense to cache partial content as the full
            response.

        :param decode_content:
            If True, will attempt to decode the body based on the
            'content-encoding' header.
        """
        ...
    
    def geturl(self):
        """
        Returns the URL that was the source of this response.
        If the request that generated this response redirected, this method
        will return the final redirect location.
        """
        ...
    
    def __iter__(self):
        ...
    


