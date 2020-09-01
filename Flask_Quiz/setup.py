try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "My Flask App",
    "author": "Ian Clark",
    "url": "bigfootpnw.tech",
    "download_url": "N/A",
    "author_email": "ianhclark510@gmail.com",
    "version": "0.1",
    "install_requires": [
        "nose",
        "click",
        "sqlalchemy",
        "flask",
        "sql",
        "dateutil",
    ],
    "scripts": [],
    "name": "todo_app",
}

setup(**config)
