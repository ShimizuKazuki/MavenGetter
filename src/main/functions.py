import git
import re
import subprocess

#Count Commit
def get_commit_count(repo):
    commits = repo.get_commits()
    return str(commits.totalCount)

def get_loc(reponame):
    a = subprocess.run(["sh", "./other/git-loc.sh", reponame], encoding='utf-8', stdout=subprocess.PIPE)
    match = re.search("SUM:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", a.stdout)
    if match is None:
        match = re.search(".+\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)", a.stdout)
    if match:
        return str(match.group(4))
    else:
        return str(0)

def get_star_count(repo):
    star = repo.get_stargazers()
    return str(star.totalCount)

