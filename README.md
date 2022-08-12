# Bump Version

Use this action to bump the major, minor, or patch version numbers in a semver
(Semantic Version) string. This action can also be used to bump the build number
of pre-release versions, eg 1.0.0-beta5

## Inputs

## `type`

**Required** one of `major`, `minor`, `patch`, `build`, or `release`.

## `version`

**Required** the semantic version string to be incremented

## Outputs

## `version`

The new version string

## Example usage

```yaml
uses: ksuderman/github-action-bump-version@v1
with:
  version: $VERSION
  type: $LABEL
```
