#!/usr/bin/env python3

import os
import re
import sys

def get_version(path: str) -> str:
    with open(path, 'r') as f:
        line = f.readline()
        if line.startswith('version:'):
            return line.split(':')[1].strip()
    return '0.0.0'


def run():
    # version_file = sys.argv[1]
    # if not os.path.exists(version_file):
    #     print("Version file not found.")
    #     sys.exit(1)
    # old_version = get_version(version_file)
    #print(sys.argv)
    type = sys.argv[1]
    version = sys.argv[2]
    print(f"Type: {type}")
    print(f"Version: {version}")    
    tagged = '-' in version
    tag = ''
    if tagged:
        parts = version.split('-')
        version = parts[0]
        (tag, patch) = parts[1].split('.')
    if type == 'simple':
        m = re.search("(\w+)(\d+)", version)
        print(f"{m.group(1)}{int(m.group(2)) + 1}")
    elif type in ['major', 'minor', 'patch']:
        semver = version.split('.')
        major = int(semver[0])
        minor = int(semver[1])
        patch = int(semver[2])
        if type == 'major':
            major += 1
            minor = 0
            patch = 0
        elif type == 'minor':
            minor += 1
            patch = 0
        elif type == 'patch':
            patch += 1
        if tagged:
            print(f"{major}.{minor}.{patch}-{tag}.1")
        else:
            print(f"{major}.{minor}.{patch}")
    elif type == 'release':
        print(version.split('-')[0])
    elif type == 'tag':
        tag = sys.argv[3]
        if tagged:
            print("ERROR: can not tag a previously tagged version.")
            sys.exit(1)
        print(f"{version}-{tag}.1")
    else:
        if type != tag:
            print(f"ERROR: No such tag {tag} type is {type}")
            return
        print(f"{version}-{tag}.{int(patch) + 1}")


if __name__ == '__main__':
    run()
