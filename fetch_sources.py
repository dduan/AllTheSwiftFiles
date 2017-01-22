'''
Shallow clone repositories specified in a json file. Then copy only the .swift
files into ./sources.

cmd argument: a json file with content in the format

[
    {"clone_url": CLONE_URL, "name": NAME},
    {"clone_url": CLONE_URL, "name": NAME},
    ...
]
'''
import os
import shutil
import sys
import json
import subprocess

if __name__ == '__main__':
    repo_file = sys.argv[1]
    repos = json.loads(open(repo_file).read())
    sources_root = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sources')
    repos_root = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'repos')
    for path in (sources_root, repos_root):
        if os.path.exists(path):
            shutil.rmtree(path)
        os.makedirs(path)

    for repo in repos:
        target_path = os.path.join(repos_root, repo['name'])
        source_path = os.path.join(sources_root, repo['name'])
        subprocess.call(['git', 'clone', '--depth', '1', repo['clone_url'], target_path])
        file_paths = subprocess.check_output(['find', target_path, '-type', 'f', '-name', '*.swift'])
        for path, opath in [(p[len(target_path)+1:], p) for p in file_paths.split('\n')]:
            if path.strip() == "":
                continue
            tpath = os.path.join(source_path, path)
            tpath_dir = os.path.dirname(tpath)
            subprocess.call(['mkdir', '-p', tpath_dir])
            if not os.path.exists(tpath):
                subprocess.call(['cp', opath, tpath])
