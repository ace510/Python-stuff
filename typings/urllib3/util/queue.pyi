"""
This type stub file was generated by pyright.
"""

from ..packages import six
from ..packages.six.moves import queue

if six.PY2:
    ...
class LifoQueue(queue.Queue):
    ...

