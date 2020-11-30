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

def run(spamwriter):
    since = "73199";
    while(True):
        reponames_since = cloner.getRepoName(since)
        since = reponames_since[1]
        print(since)
        g = Github()
        for reponame in reponames_since[0]:
            print(reponame)
            out = []
            cloner.cloneRepo(reponame)
            if not os.path.exists(cloner.repoDir + reponame + "/pom.xml"):
                logging.info(reponame + " is not Maven Project")
                shutil.rmtree(cloner.repoDir + reponame.split('/')[0])
                continue
            repo = g.get_repo(reponame)
            out.append("https://github.com/" + reponame + " ")
            logging.info(reponame + " #commit: " + functions.get_commit_count(repo))
            out.append(functions.get_commit_count(repo))
            logging.info(reponame + " #loc: " + functions.get_loc(reponame))
            out.append(functions.get_loc(reponame))
            logging.info(reponame + " #star: " + functions.get_star_count(repo))
            out.append(functions.get_star_count(repo))
            spamwriter.writerow(out)
            shutil.rmtree(cloner.repoDir + reponame.split('/')[0])

def main():
    try:
        with open(f'outputs/projects.csv', 'a') as f:
            spamwriter = csv.writer(f, delimiter=',', quotechar='|')
            run(spamwriter)
    except Exception as e:
        logging.error(e)
        

if __name__ == '__main__':
    main()
