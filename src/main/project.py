import re
import subprocess
from concurrent.futures.thread import ThreadPoolExecutor
import csv
import time
import pandas as pd

import repositoryCloner as cloner

#Count Commit
def get_commit_count(repo):
    commits = repo.get_commits()
    return commits.totalCount

def main():
    reponames = cloner.getRepoName()

if __name__ == '__main__':
    main()
