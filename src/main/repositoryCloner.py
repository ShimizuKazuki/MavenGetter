import tempfile
import shutil
import random
import git
import traceback
import urllib.request, urllib.error
import logging
import subprocess
import pandas as pd

repoDir = "repos/"
logging.basicConfig(level=logging.DEBUG)


def getRepoName():
    csv_input = pd.read_csv(filepath_or_buffer="input/project_list.csv", sep=",")
    
    return csv_input['name'].tolist()

def cloneRepo(reponame):
    try: 
        a = subprocess.run(["sh", "./other/clone.sh", reponame], encoding='utf-8', stdout=subprocess.PIPE)
    except:
        logging.error(reponame + " cannot be cloned")
        traceback.print_exc()