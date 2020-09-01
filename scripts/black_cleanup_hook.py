import os
from os.path import join
from pathlib import Path
import logging
import subprocess

logging.basicConfig( 
    level=logging.DEBUG)
PATH_DIR = "D:\\Python-stuff"


noticed_scripts = set()

for root, dirs, files in os.walk(PATH_DIR):
    for name in files:
        if Path(name).suffix == '.py':
            logging.debug(walrus  := join(root,name))
            noticed_scripts.add(walrus)

for fp in noticed_scripts:
    subprocess.run(['black', fp], check=True)