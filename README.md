# Bump Version

Use this action to bump the major, minor, or patch version numbers in a semver
(Semantic Version) string. This action can also be used to bump the build number
of pre-release versions, eg 1.0.0-beta.5

## Inputs

- `type`<br/>
   **Required** one of `simple`, `major`, `minor`, `patch` or a string representing a pre-release type (e.g. `dev` or `rc`)
- `parser`<br/>
   **Required** the shell command used to extract the current version number.  Must be one of `awk` or `cat`.
- `file`<br/>
   **Required** the path to the file containing the version number.

## Notes

The version `file` should contain the string `version: x.y.z` on a line by itself (awk), or should contain a single line with the version number (cat).

## Example usage

Update the version in a Helm Chart
```yaml
uses: ksuderman/github-action-bump-version@v2
with:
  type: ${{ join(github.event.pull_request.labels.*.name, ' ') }}
  parser: awk
  file: Chart.yaml
```

Update the version in a VERSION file or similar
```yaml
uses: ksuderman/github-action-bump-version@v2
with:
  type: ${{ join(github.event.pull_request.labels.*.name, ' ') }}
  parser: cat
  file: VERSION
```

How we [eat our own dog food](https://github.com/ksuderman/github-action-bump-version/blob/master/.github/workflows/release.yml).
```yaml
- uses: ksuderman/github-action-bump-version@dev
  env:
    GITHUB_TOKEN: ${{ github.token }}
  with:
    file: VERSION
    parser: cat
    type: simple```
```

**Note** We use the `dev` version on ourselves since, by definition, the one in `master` or any tagged version is out of date.

