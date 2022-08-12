#!/usr/bin/env python3

import re
import sys

type = sys.argv[1]
version = sys.argv[2]

is_prerelease = '-' in version

if type in ['major', 'minor', 'patch'] and is_prerelease:
    print("ERROR: can not bump the semver of a pre-release version. Use the 'release' type.")
    sys.exit(1)

semver = version.split('.')
major = int(semver[0])
minor = int(semver[1])
patch = semver[2]

if is_prerelease:
    parts = patch.split('-')
    patch = int(parts[0])
    regex = re.search('([a-zA-Z]+)([0-9]+)', parts[1])
    prerelease = regex.group(1)
    build = int(regex.group(2))
    if type == 'build':
        build += 1
        print(f"{major}.{minor}.{patch}-{prerelease}{build}")
    elif type == 'release':
        print(f"{major}.{minor}.{patch}")
        pass
    else:
        print(f"ERROR: Invalid bump type {type}")
        sys.exit(1)
elif type == 'major':
    major += 1
    minor = 0
    patch = 0
elif type == 'minor':
    minor += 1
    patch = 0
elif type == 'patch':
    patch += 1
else:
    print("ERROR: Invalid parameter: {type}")
    sys.exit(1)

print(f"::set-output name=version::{major}.{minor}.{patch}")
