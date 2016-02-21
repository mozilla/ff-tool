# ff-tool
ff-tool is a Python CLI tool for downloading desktop Firefox versions, 
as well as managing profiles and test prefs.  It is largely a glorified 
convenience wrapper we'ver written around these amazing tools/libraries:

* [mozdownload](https://github.com/mozilla/mozdownload)
* [mozprofile](https://github.com/mozilla/mozprofile)


:bangbang: _NOTE: This tool is work in progress...  DO NOT USE_ :bangbang:


# Installation

## Pre-requisites
* ff-tool requires you have python and virtualenv installed.

## Build
```
$ make build
$ source ./venv/bin/activate
```

## Cleanup
```
$ deactivate
$ make clean 
```

# Run
## Example(s)
```
$ ff -h
$ ff download -h
$ ff download -c nightly
```

