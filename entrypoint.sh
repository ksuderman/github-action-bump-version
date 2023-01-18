#!/usr/bin/env bash
set -eu

#type=$(echo $1 | awk \
#  '/major/{ print "major"; exit}
#  /minor/{print "minor" ; exit}
#  /patch/{print "patch" ; exit}')

type=$1
parser=$2
version_file=$3

if [[ ! -e $version_file ]] ; then
  echo "File not found $version_file"
  exit 1
fi

if [[ $parser == 'awk' ]] ; then
  current_version=$(awk '/^version:/{ print $2 }' $version_file)
elif [[ $parser == 'cat' ]] ; then
  current_version=$(cat $version_file)
else
  echo "Invalid option: '$parser'"
  echo "Must be one of [awk|cat]"
  exit 1
fi
echo "Current version is $current_version"
new_version=$(python3 /bump.py $type $current_version)

if [[ $parser == 'awk' ]] ; then
  tmp=$(mktemp)
  sed "s/^version:.*/version: $new_version/" $version_file > $tmp
  mv $tmp $version_file
else
  echo $new_version > $version_file
fi

git config --global --add safe.directory /github/workspace
git config --global user.email $(git --no-pager log --format=format:'%ae' -n 1)
git config --global user.name $(git --no-pager log --format=format:'%an' -n 1)

git add $version_file
git commit -m "Automatic version bump to $new_version"
branch=$(git branch | awk '/\*/{print $2}')
echo "Pushing branch $branch"
git push origin $branch
echo "Updated version from $current_version to $new_version"

