# CHANGELOG

## v1.2.0

### Feature
- custom cz plugins now support bumping version

## v1.1.1

### Fix
- breaking change is now part of the body, instead of being in the subject

## v1.1.0

### Features
- auto bump version based on conventional commits using sem ver
- pyproject support (see [pyproject.toml](./pyproject.toml) for usage)

## v1.0.0

### Features
- more documentation
- added tests
- support for conventional commits 1.0.0

### BREAKING CHANGES
- use of questionary to generate the prompt (so we depend on promptkit 2.0)
- python 3 only
