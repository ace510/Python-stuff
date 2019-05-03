import nose.tools
import ..blog

def setup_blog():



@with_setup(setup_blog):
def test_index():
    blog.index()