import os
from pathlib import Path ## to handle the forward / inwindow we uuse pathlib library
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')


project_name = "cnnClassifier"


list_of_files =[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/_init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trail.ipynb"
]

## logic
for filepath in list_of_files:
    filepath = Path(filepath) ## inserting filepath in Path class which will gives us windows path
    filedir, filename = os.path.split(filepath)## splitting folder and file

    if filedir !="": # if folder is not empty (creating folder)
        os.makedirs(filedir, exist_ok=True) ##if it exists it wont be created
        logging.info("Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): ##creating file (if file doesnot exist or file size is zero then it will replace that one with new file)
        with open(filepath, 'w') as f:
            pass ## creating an empty file only
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is alrady exist")




    
