import tempfile
import shutil
import random
import git
import traceback
import urllib.request, urllib.error
import logging
import subprocess

repoDir= 'repos/'
logging.basicConfig(level=logging.DEBUG)


def getRepoName(since):
    reponames = []
    with urllib.request.urlopen("https://api.github.com/repositories?since=" + since) as response:
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            shutil.copyfileobj(response, temp_file)
            with open(temp_file.name) as f:
                content = f.read()
                id = [s for s in content.split(',') if '{"id"' in s]
                last_id = id[-1].split(":")[1].strip('"')
                print(last_id)
                full_names = [s for s in content.split(',') if "full_name" in s]
                for full_name in full_names:
                    reponame = full_name.split(":")[1].strip('"')
                    reponames.append(reponame)
    return reponames, last_id

def cloneRepo(reponame):
    try: 
        a = subprocess.run(["sh", "./other/clone.sh", reponame], encoding='utf-8', stdout=subprocess.PIPE)
    except:
        logging.error(reponame + " cannot be cloned")
        traceback.print_exc()