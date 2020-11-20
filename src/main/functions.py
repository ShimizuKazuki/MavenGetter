import git

#Count Commit
def get_commit_count(repo):
    commits = repo.get_commits()
    return commits.totalCount

