import os
from pathlib import Path
import logging

# Correct logging level to logging.INFO
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "Text summarizer"

list_of_files =[
    ".github/workflows/.getkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  
    f"src/{project_name}/utils/__init__.py",       
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",    
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/configuration.py", 
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb" ,
    "Dockerfile",
    "app.py",
]

for file in list_of_files:
    file = Path(file)
    filedir, filename = os.path.split(file)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")
    
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        with open(file, 'w') as f:  # Changed to 'w' mode to create the file
            pass
        logging.info(f"Created empty file: {filename}")
    else:
        logging.info(f"File {filename} already exists.")

