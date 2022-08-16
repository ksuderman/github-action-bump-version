# Bump Version

Use this action to bump the major, minor, or patch version numbers in a semver
(Semantic Version) string. This action can also be used to bump the build number
of pre-release versions, eg 1.0.0-beta5

## Inputs

## `type`

**Required** one of `major`, `minor`, `patch`

## `command`

**Required** the shell command used to extract the current version number.  Must be one of `awk` or `cat`.

## `file`

**Required** the path to the file containing the version number.

## Notes

The version `file` should contain the string `version: x.y.z` on a line by itself (awk), or should contain a single line with the version number (cat).

## Example usage

Update the version in a Helm Chart
```yaml
uses: ksuderman/github-action-bump-version@v1
with:
  type: ${{ join(github.event.pull_request.labels.*.name, ' ') }}
  command: awk
  file: Chart.yaml
```

Update the version in a VERSION file or similar
```yaml
uses: ksuderman/github-action-bump-version@v1
with:
  type: ${{ join(github.event.pull_request.labels.*.name, ' ') }}
  command: cat
  file: VERSION
```

