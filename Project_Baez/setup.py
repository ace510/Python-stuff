try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Project Baez',
    'author': 'Ian Clark',
    'url':'N/A',
    'download_url':'N/A',
    'author_email':'ianhclark510@gmail.com',
    'version': '0.1',
    'install_requires':['nose','click','sqlalchemy','flask','sql','python-dateutil',],
    'scripts':[],
    'name': 'Project_Baez'
}

setup(**config)