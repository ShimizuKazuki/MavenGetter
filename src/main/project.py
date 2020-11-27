import re
import subprocess
from concurrent.futures.thread import ThreadPoolExecutor
import csv
import time
import pandas as pd
import os
import shutil
import logging
from github import Github
from github.GithubException import UnknownObjectException

import repositoryCloner as cloner
import functions

logging.basicConfig(level=logging.DEBUG)

def main():
    try:
        reponames = cloner.getRepoName()
        g = Github()
        for reponame in reponames:
            out = []
            cloner.cloneRepo(reponame)
            print(cloner.repoDir + reponame + "/pom.xml")
            if not os.path.exists(cloner.repoDir + reponame + "/pom.xml"):
                logging.info(reponame + " is not Maven Project")
                shutil.rmtree(cloner.repoDir + reponame.split('/')[0])
                #continue; #For Debug
            repo = g.get_repo(reponame)
            logging.info(reponame + " #commit: " + str(functions.get_commit_count(repo)))
            out.append(str(functions.get_commit_count(repo)))
            a = subprocess.run(["sh", "./other/git-loc.sh", reponame], encoding='utf-8', stdout=subprocess.PIPE)
            match = re.search("SUM:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", a.stdout)
            if match is None:
                match = re.search(".+\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", a.stdout)
            if match:
                out.append(str(match.group(1)))# files
                out.append(str(match.group(4)))# code
            else:
                out.append(str(0))# files
                out.append(str(0))# code
            break
    except UnknownObjectException:
        logging.error(reponame + " not found:404")
        

if __name__ == '__main__':
    main()
