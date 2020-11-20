import tempfile
import shutil
import random
import git
import traceback
import urllib.request, urllib.error
import logging

repoDir= 'repos/input/'
logging.basicConfig(level=logging.DEBUG)

def random_value():
    return str(int(random.uniform(1, 50000)))

def getRepoName():
    reponames = []
    #TODO:Use ID to get repository
    with urllib.request.urlopen("https://api.github.com/repositories?since=" + random_value()) as response:
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            shutil.copyfileobj(response, temp_file)
            with open(temp_file.name) as f:
                content = f.read()
                full_names = [s for s in content.split(',') if "full_name" in s]
                for full_name in full_names:
                    reponame = full_name.split(":")[1].strip('"')
                    reponames.append(reponame)
    return reponames

def cloneRepo(reponame):
    try: 
        git.Git().clone("https://github.com/" + reponame, repoDir+reponame)
    except:
        logging.error(reponame + " cannot be cloned")
        traceback.print_exc()