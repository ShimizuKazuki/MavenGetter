import os
import csv

project_list_path = './outputs/project_list.csv'

def pj_file_factory(reponame):
    path = './outputs/pjs/' + reponame.split('/')[1] + '.pj'
    f = open(path, 'w')
    f.write('name=' + reponame.split('/')[1] + '\r\n' +
            'abb=ACT\r\n' + 
            'url=https://github.com/' + reponame + '\r\n' +
            'branch=master')
    f.close()

def main():
    with open('outputs/projects.csv') as f:
        reponames = csv.reader(f)
        for reponame in reponames:
            pj_file_factory(reponame[0])


if __name__ == '__main__':
    main()