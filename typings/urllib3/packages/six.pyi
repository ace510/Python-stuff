"""
This type stub file was generated by pyright.
"""

import functools
import itertools
import operator
import sys
import types
import struct
import io
import StringIO

"""Utilities for writing code that runs on Python 2 and 3"""
__author__ = "Benjamin Peterson <benjamin@python.org>"
__version__ = "1.12.0"
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
PY34 = sys.version_info[0: 2] >= (3, 4)
if PY3:
    string_types = (str, )
    integer_types = (int, )
    class_types = (type, )
    text_type = str
    binary_type = bytes
    MAXSIZE = sys.maxsize
else:
    string_types = (basestring, )
    integer_types = (int, long)
    class_types = (type, types.ClassType)
    text_type = unicode
    binary_type = str
class _LazyDescr(object):
    def __init__(self, name) -> None:
        ...
    
    def __get__(self, obj, tp):
        ...
    


class MovedModule(_LazyDescr):
    def __init__(self, name, old, new=...) -> None:
        ...
    
    def __getattr__(self, attr):
        ...
    


class _LazyModule(types.ModuleType):
    def __init__(self, name) -> None:
        ...
    
    def __dir__(self):
        ...
    
    _moved_attributes = ...


class MovedAttribute(_LazyDescr):
    def __init__(self, name, old_mod, new_mod, old_attr=..., new_attr=...) -> None:
        ...
    


class _SixMetaPathImporter(object):
    """
    A meta path importer to import six.moves and its submodules.

    This class implements a PEP302 finder and loader. It should be compatible
    with Python 2.5 and all existing versions of Python3
    """
    def __init__(self, six_module_name) -> None:
        ...
    
    def find_module(self, fullname, path=...):
        ...
    
    def load_module(self, fullname):
        ...
    
    def is_package(self, fullname):
        """
        Return true, if the named module is a package.

        We need this method to get correct spec objects with
        Python 3.4 (see PEP451)
        """
        ...
    
    def get_code(self, fullname):
        """Return None

        Required, if is_package is implemented"""
        ...
    
    get_source = ...


_importer = _SixMetaPathImporter(__name__)
class _MovedItems(_LazyModule):
    """Lazy loading of moved objects"""
    __path__ = ...


_moved_attributes = [MovedAttribute("cStringIO", "cStringIO", "io", "StringIO"), MovedAttribute("filter", "itertools", "builtins", "ifilter", "filter"), MovedAttribute("filterfalse", "itertools", "itertools", "ifilterfalse", "filterfalse"), MovedAttribute("input", "__builtin__", "builtins", "raw_input", "input"), MovedAttribute("intern", "__builtin__", "sys"), MovedAttribute("map", "itertools", "builtins", "imap", "map"), MovedAttribute("getcwd", "os", "os", "getcwdu", "getcwd"), MovedAttribute("getcwdb", "os", "os", "getcwd", "getcwdb"), MovedAttribute("getoutput", "commands", "subprocess"), MovedAttribute("range", "__builtin__", "builtins", "xrange", "range"), MovedAttribute("reload_module", "__builtin__", "importlib" if PY34 else "imp", "reload"), MovedAttribute("reduce", "__builtin__", "functools"), MovedAttribute("shlex_quote", "pipes", "shlex", "quote"), MovedAttribute("StringIO", "StringIO", "io"), MovedAttribute("UserDict", "UserDict", "collections"), MovedAttribute("UserList", "UserList", "collections"), MovedAttribute("UserString", "UserString", "collections"), MovedAttribute("xrange", "__builtin__", "builtins", "xrange", "range"), MovedAttribute("zip", "itertools", "builtins", "izip", "zip"), MovedAttribute("zip_longest", "itertools", "itertools", "izip_longest", "zip_longest"), MovedModule("builtins", "__builtin__"), MovedModule("configparser", "ConfigParser"), MovedModule("copyreg", "copy_reg"), MovedModule("dbm_gnu", "gdbm", "dbm.gnu"), MovedModule("_dummy_thread", "dummy_thread", "_dummy_thread"), MovedModule("http_cookiejar", "cookielib", "http.cookiejar"), MovedModule("http_cookies", "Cookie", "http.cookies"), MovedModule("html_entities", "htmlentitydefs", "html.entities"), MovedModule("html_parser", "HTMLParser", "html.parser"), MovedModule("http_client", "httplib", "http.client"), MovedModule("email_mime_base", "email.MIMEBase", "email.mime.base"), MovedModule("email_mime_image", "email.MIMEImage", "email.mime.image"), MovedModule("email_mime_multipart", "email.MIMEMultipart", "email.mime.multipart"), MovedModule("email_mime_nonmultipart", "email.MIMENonMultipart", "email.mime.nonmultipart"), MovedModule("email_mime_text", "email.MIMEText", "email.mime.text"), MovedModule("BaseHTTPServer", "BaseHTTPServer", "http.server"), MovedModule("CGIHTTPServer", "CGIHTTPServer", "http.server"), MovedModule("SimpleHTTPServer", "SimpleHTTPServer", "http.server"), MovedModule("cPickle", "cPickle", "pickle"), MovedModule("queue", "Queue"), MovedModule("reprlib", "repr"), MovedModule("socketserver", "SocketServer"), MovedModule("_thread", "thread", "_thread"), MovedModule("tkinter", "Tkinter"), MovedModule("tkinter_dialog", "Dialog", "tkinter.dialog"), MovedModule("tkinter_filedialog", "FileDialog", "tkinter.filedialog"), MovedModule("tkinter_scrolledtext", "ScrolledText", "tkinter.scrolledtext"), MovedModule("tkinter_simpledialog", "SimpleDialog", "tkinter.simpledialog"), MovedModule("tkinter_tix", "Tix", "tkinter.tix"), MovedModule("tkinter_ttk", "ttk", "tkinter.ttk"), MovedModule("tkinter_constants", "Tkconstants", "tkinter.constants"), MovedModule("tkinter_dnd", "Tkdnd", "tkinter.dnd"), MovedModule("tkinter_colorchooser", "tkColorChooser", "tkinter.colorchooser"), MovedModule("tkinter_commondialog", "tkCommonDialog", "tkinter.commondialog"), MovedModule("tkinter_tkfiledialog", "tkFileDialog", "tkinter.filedialog"), MovedModule("tkinter_font", "tkFont", "tkinter.font"), MovedModule("tkinter_messagebox", "tkMessageBox", "tkinter.messagebox"), MovedModule("tkinter_tksimpledialog", "tkSimpleDialog", "tkinter.simpledialog"), MovedModule("urllib_parse", __name__ + ".moves.urllib_parse", "urllib.parse"), MovedModule("urllib_error", __name__ + ".moves.urllib_error", "urllib.error"), MovedModule("urllib", __name__ + ".moves.urllib", __name__ + ".moves.urllib"), MovedModule("urllib_robotparser", "robotparser", "urllib.robotparser"), MovedModule("xmlrpc_client", "xmlrpclib", "xmlrpc.client"), MovedModule("xmlrpc_server", "SimpleXMLRPCServer", "xmlrpc.server")]
if sys.platform == "win32":
    ...
moves = _MovedItems(__name__ + ".moves")
class Module_six_moves_urllib_parse(_LazyModule):
    """Lazy loading of moved objects in six.moves.urllib_parse"""
    ...


_urllib_parse_moved_attributes = [MovedAttribute("ParseResult", "urlparse", "urllib.parse"), MovedAttribute("SplitResult", "urlparse", "urllib.parse"), MovedAttribute("parse_qs", "urlparse", "urllib.parse"), MovedAttribute("parse_qsl", "urlparse", "urllib.parse"), MovedAttribute("urldefrag", "urlparse", "urllib.parse"), MovedAttribute("urljoin", "urlparse", "urllib.parse"), MovedAttribute("urlparse", "urlparse", "urllib.parse"), MovedAttribute("urlsplit", "urlparse", "urllib.parse"), MovedAttribute("urlunparse", "urlparse", "urllib.parse"), MovedAttribute("urlunsplit", "urlparse", "urllib.parse"), MovedAttribute("quote", "urllib", "urllib.parse"), MovedAttribute("quote_plus", "urllib", "urllib.parse"), MovedAttribute("unquote", "urllib", "urllib.parse"), MovedAttribute("unquote_plus", "urllib", "urllib.parse"), MovedAttribute("unquote_to_bytes", "urllib", "urllib.parse", "unquote", "unquote_to_bytes"), MovedAttribute("urlencode", "urllib", "urllib.parse"), MovedAttribute("splitquery", "urllib", "urllib.parse"), MovedAttribute("splittag", "urllib", "urllib.parse"), MovedAttribute("splituser", "urllib", "urllib.parse"), MovedAttribute("splitvalue", "urllib", "urllib.parse"), MovedAttribute("uses_fragment", "urlparse", "urllib.parse"), MovedAttribute("uses_netloc", "urlparse", "urllib.parse"), MovedAttribute("uses_params", "urlparse", "urllib.parse"), MovedAttribute("uses_query", "urlparse", "urllib.parse"), MovedAttribute("uses_relative", "urlparse", "urllib.parse")]
class Module_six_moves_urllib_error(_LazyModule):
    """Lazy loading of moved objects in six.moves.urllib_error"""
    ...


_urllib_error_moved_attributes = [MovedAttribute("URLError", "urllib2", "urllib.error"), MovedAttribute("HTTPError", "urllib2", "urllib.error"), MovedAttribute("ContentTooShortError", "urllib", "urllib.error")]
class Module_six_moves_urllib_request(_LazyModule):
    """Lazy loading of moved objects in six.moves.urllib_request"""
    ...


_urllib_request_moved_attributes = [MovedAttribute("urlopen", "urllib2", "urllib.request"), MovedAttribute("install_opener", "urllib2", "urllib.request"), MovedAttribute("build_opener", "urllib2", "urllib.request"), MovedAttribute("pathname2url", "urllib", "urllib.request"), MovedAttribute("url2pathname", "urllib", "urllib.request"), MovedAttribute("getproxies", "urllib", "urllib.request"), MovedAttribute("Request", "urllib2", "urllib.request"), MovedAttribute("OpenerDirector", "urllib2", "urllib.request"), MovedAttribute("HTTPDefaultErrorHandler", "urllib2", "urllib.request"), MovedAttribute("HTTPRedirectHandler", "urllib2", "urllib.request"), MovedAttribute("HTTPCookieProcessor", "urllib2", "urllib.request"), MovedAttribute("ProxyHandler", "urllib2", "urllib.request"), MovedAttribute("BaseHandler", "urllib2", "urllib.request"), MovedAttribute("HTTPPasswordMgr", "urllib2", "urllib.request"), MovedAttribute("HTTPPasswordMgrWithDefaultRealm", "urllib2", "urllib.request"), MovedAttribute("AbstractBasicAuthHandler", "urllib2", "urllib.request"), MovedAttribute("HTTPBasicAuthHandler", "urllib2", "urllib.request"), MovedAttribute("ProxyBasicAuthHandler", "urllib2", "urllib.request"), MovedAttribute("AbstractDigestAuthHandler", "urllib2", "urllib.request"), MovedAttribute("HTTPDigestAuthHandler", "urllib2", "urllib.request"), MovedAttribute("ProxyDigestAuthHandler", "urllib2", "urllib.request"), MovedAttribute("HTTPHandler", "urllib2", "urllib.request"), MovedAttribute("HTTPSHandler", "urllib2", "urllib.request"), MovedAttribute("FileHandler", "urllib2", "urllib.request"), MovedAttribute("FTPHandler", "urllib2", "urllib.request"), MovedAttribute("CacheFTPHandler", "urllib2", "urllib.request"), MovedAttribute("UnknownHandler", "urllib2", "urllib.request"), MovedAttribute("HTTPErrorProcessor", "urllib2", "urllib.request"), MovedAttribute("urlretrieve", "urllib", "urllib.request"), MovedAttribute("urlcleanup", "urllib", "urllib.request"), MovedAttribute("URLopener", "urllib", "urllib.request"), MovedAttribute("FancyURLopener", "urllib", "urllib.request"), MovedAttribute("proxy_bypass", "urllib", "urllib.request"), MovedAttribute("parse_http_list", "urllib2", "urllib.request"), MovedAttribute("parse_keqv_list", "urllib2", "urllib.request")]
class Module_six_moves_urllib_response(_LazyModule):
    """Lazy loading of moved objects in six.moves.urllib_response"""
    ...


_urllib_response_moved_attributes = [MovedAttribute("addbase", "urllib", "urllib.response"), MovedAttribute("addclosehook", "urllib", "urllib.response"), MovedAttribute("addinfo", "urllib", "urllib.response"), MovedAttribute("addinfourl", "urllib", "urllib.response")]
class Module_six_moves_urllib_robotparser(_LazyModule):
    """Lazy loading of moved objects in six.moves.urllib_robotparser"""
    ...


_urllib_robotparser_moved_attributes = [MovedAttribute("RobotFileParser", "robotparser", "urllib.robotparser")]
class Module_six_moves_urllib(types.ModuleType):
    """Create a six.moves.urllib namespace that resembles the Python 3 namespace"""
    __path__ = ...
    parse = ...
    error = ...
    request = ...
    response = ...
    robotparser = ...
    def __dir__(self):
        ...
    


def add_move(move):
    """Add an item to six.moves."""
    ...

def remove_move(name):
    """Remove item from six.moves."""
    ...

if PY3:
    _meth_func = "__func__"
    _meth_self = "__self__"
    _func_closure = "__closure__"
    _func_code = "__code__"
    _func_defaults = "__defaults__"
    _func_globals = "__globals__"
else:
    _meth_func = "im_func"
    _meth_self = "im_self"
    _func_closure = "func_closure"
    _func_code = "func_code"
    _func_defaults = "func_defaults"
    _func_globals = "func_globals"
next = advance_iterator
if PY3:
    def get_unbound_function(unbound):
        ...
    
    create_bound_method = types.MethodType
    def create_unbound_method(func, cls):
        ...
    
    Iterator = object
else:
    def get_unbound_function(unbound):
        ...
    
    def create_bound_method(func, obj):
        ...
    
    def create_unbound_method(func, cls):
        ...
    
    class Iterator(object):
        def next(self):
            ...
        
    
    
    callable = callable
get_method_function = operator.attrgetter(_meth_func)
get_method_self = operator.attrgetter(_meth_self)
get_function_closure = operator.attrgetter(_func_closure)
get_function_code = operator.attrgetter(_func_code)
get_function_defaults = operator.attrgetter(_func_defaults)
get_function_globals = operator.attrgetter(_func_globals)
if PY3:
    def iterkeys(d, **kw):
        ...
    
    def itervalues(d, **kw):
        ...
    
    def iteritems(d, **kw):
        ...
    
    def iterlists(d, **kw):
        ...
    
    viewkeys = operator.methodcaller("keys")
    viewvalues = operator.methodcaller("values")
    viewitems = operator.methodcaller("items")
else:
    def iterkeys(d, **kw):
        ...
    
    def itervalues(d, **kw):
        ...
    
    def iteritems(d, **kw):
        ...
    
    def iterlists(d, **kw):
        ...
    
    viewkeys = operator.methodcaller("viewkeys")
    viewvalues = operator.methodcaller("viewvalues")
    viewitems = operator.methodcaller("viewitems")
if PY3:
    def b(s):
        ...
    
    def u(s):
        ...
    
    unichr = chr
    int2byte = struct.Struct(">B").pack
    byte2int = operator.itemgetter(0)
    indexbytes = operator.getitem
    iterbytes = iter
    StringIO = io.StringIO
    BytesIO = io.BytesIO
    _assertCountEqual = "assertCountEqual"
else:
    def b(s):
        ...
    
    def u(s):
        ...
    
    unichr = unichr
    int2byte = chr
    def byte2int(bs):
        ...
    
    def indexbytes(buf, i):
        ...
    
    iterbytes = functools.partial(itertools.imap, ord)
    StringIO = BytesIO = StringIO.StringIO
    _assertCountEqual = "assertItemsEqual"
    _assertRaisesRegex = "assertRaisesRegexp"
    _assertRegex = "assertRegexpMatches"
def assertCountEqual(self, *args, **kwargs):
    ...

def assertRaisesRegex(self, *args, **kwargs):
    ...

def assertRegex(self, *args, **kwargs):
    ...

if PY3:
    exec_ = getattr(moves.builtins, "exec")
    def reraise(tp, value, tb=...):
        ...
    
else:
    def exec_(_code_, _globs_=..., _locs_=...):
        """Execute code in a namespace."""
        ...
    
if sys.version_info[: 2] == (3, 2):
    ...
else:
    def raise_from(value, from_value):
        ...
    
print_ = getattr(moves.builtins, "print", None)
if print_ is None:
    def print_(*args, **kwargs):
        """The new-style print function for Python 2.4 and 2.5."""
        ...
    
if sys.version_info[: 2] < (3, 3):
    _print = print_
    def print_(*args, **kwargs):
        ...
    
if sys.version_info[0: 2] < (3, 4):
    def wraps(wrapped, assigned=..., updated=...):
        ...
    
else:
    wraps = functools.wraps
def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    class metaclass(type):
        ...
    
    

def add_metaclass(metaclass):
    """Class decorator for creating a class with a metaclass."""
    ...

def ensure_binary(s, encoding=..., errors=...):
    """Coerce **s** to six.binary_type.

    For Python 2:
      - `unicode` -> encoded to `str`
      - `str` -> `str`

    For Python 3:
      - `str` -> encoded to `bytes`
      - `bytes` -> `bytes`
    """
    ...

def ensure_str(s, encoding=..., errors=...):
    """Coerce *s* to `str`.

    For Python 2:
      - `unicode` -> encoded to `str`
      - `str` -> `str`

    For Python 3:
      - `str` -> `str`
      - `bytes` -> decoded to `str`
    """
    ...

def ensure_text(s, encoding=..., errors=...):
    """Coerce *s* to six.text_type.

    For Python 2:
      - `unicode` -> `unicode`
      - `str` -> `unicode`

    For Python 3:
      - `str` -> `str`
      - `bytes` -> decoded to `str`
    """
    ...

def python_2_unicode_compatible(klass):
    """
    A decorator that defines __unicode__ and __str__ methods under Python 2.
    Under Python 3 it does nothing.

    To support Python 2 and 3 with a single code base, define a __str__ method
    returning text and apply this decorator to the class.
    """
    ...

__path__ = []
__package__ = __name__
if globals().get("__spec__") is not None:
    ...
if sys.meta_path:
    ...
