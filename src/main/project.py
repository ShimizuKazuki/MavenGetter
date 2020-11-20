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
            #Maven Project should be Deleted
            print(cloner.repoDir + reponame + "/pom.xml")
            # if not os.path.exists(cloner.repoDir + reponame + "pom.xml"):
            #     logging.info(reponame + " is not Maven Project")
            #     shutil.rmtree(cloner.repoDir + reponame.split('/')[0])
            repo = g.get_repo(reponame)
            logging.info(reponame + " #commit: " + str(functions.get_commit_count(repo)))
            out.append(str(functions.get_commit_count(repo)))
            break
    except UnknownObjectException:
        logging.error(reponame + " not found:404")
        

if __name__ == '__main__':
    main()
