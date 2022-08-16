#!/usr/bin/env bash
set -eu

type=$(echo $1 | awk \
  '/major/{ print "major"; exit}
  /minor/{print "minor" ; exit}
  /patch/{print "patch" ; exit}')

command=$2
version_file=$3

if [[ ! -e $version_file ]] ; then
  echo "File not found $version_file"
  exit 1
fi

if [[ $command == 'awk' ]] ; then
  current_version=$(awk '/^version:/{ print $2 }' $version_file)
elif [[ $command == 'cat' ]] ; then
  current_version=$(cat $version_file)
else
  echo "Invalid option: $command"
  echo "Must be one of [awk|cat]"
  exit 1
fi

new_version=$(python3 /bump.py $type $current_version)

if [[ $command == 'awk' ]] ; then
  tmp=$(mktemp)
  sed "s/^version:.*/version: $new_version/" $version_file > $tmp
  mv $tmp $version_file
else
  echo $new_version > $version_file
fi

git add $version_file
git commit -m "Automatic version bump to $new_version"
branch=$(git branch | awk '/\*/{print $2}')
git push origin $branch
echo "Updated version from $current_version to $new_version"

