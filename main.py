from git import Repo
from glob import glob
import subprocess
import shlex
import os
import argparse
import datetime
from dateutil import relativedelta
from git.util import Stats

def main():

    print("Test 1 2 3")

    # remote_url = "git@github.com:subhash-vadlamani/nova.git"
    local_folder = "/tmp/nova"

    # myrepo = Repo.clone_from(remote_url, local_folder)
    myrepo = Repo(local_folder)

    commits = list(myrepo.iter_commits( since='six months', paths='E:/tmp/nova/nova'))
    print(len(commits))
    directories = glob('E:/tmp/nova/nova/*/')
    print(directories)
    commit_length_dict = {}
    commit_list = {}
    for directory in directories:
        commit_list[directory] = list(myrepo.iter_commits('HEAD', since='six months', paths=directory))
        commit_length_dict[directory] = len(list(myrepo.iter_commits('HEAD', since='six months', paths=directory)))
    sort_commit_list = sorted(commit_length_dict.items(), key=lambda x: x[1], reverse=True)
    print(sort_commit_list)
    print((sort_commit_list[:12]))

    churn = {}

    for directory in directories:
        print("###################")
        print("directory : {}".format(directory))
        print(commit_length_dict[directory])
        churn[directory] = 0
        for commit in commit_list[directory]:
            string_directory = directory.replace("\\", "/")
            string_directory_list = string_directory.split('/',3)
            directory_key = string_directory_list[3]
            s = commit.stats
            files = s.files
            for entry in files:

                if entry.startswith(directory_key):
                    churn[directory] += files[entry]['lines']
        # print(churn)
        print("#############")
    print(churn)

    sorted_churn_list = sorted(churn.items(), key=lambda x: x[1], reverse=True)
    print(sorted_churn_list)
    print((sorted_churn_list[:12]))