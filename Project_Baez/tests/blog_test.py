import nose.tools
from .. import blog


def setup_blog():
    pass


# @with_setup(setup_blog):


def text_index():
    blog.index()
