import re
import subprocess
from concurrent.futures.thread import ThreadPoolExecutor
import csv
import time
import pandas as pd
import os
import shutil
import logging

import repositoryCloner as cloner

logging.basicConfig(level=logging.DEBUG)

#Count Commit
def get_commit_count(repo):
    commits = repo.get_commits()
    return commits.totalCount

def main():
    reponames = cloner.getRepoName()
    for reponame in reponames:
        cloner.cloneRepo(reponame)
        #Maven Project should be Deleted
        print(cloner.repoDir + reponame + "/pom.xml")
        if not os.path.exists(cloner.repoDir + reponame + "pom.xml"):
            logging.info(reponame + " is not Maven Project")
            shutil.rmtree(cloner.repoDir + reponame.split('/')[0])

        

if __name__ == '__main__':
    main()
