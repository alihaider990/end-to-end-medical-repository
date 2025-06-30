import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

list_of_files = [
    "src/__init__.py",
    "srchelper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]


for filepath in list_of_files:
    filepath = path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.markedirs(filedir,exist_ok=true)
        logging.info(f"creating directory; {filedir} for the file: {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, 'w') as f:
                pass

            logging.info(f"creating empty file: {filepath}")

        else:
            logging.info(f"{filename} already exists")