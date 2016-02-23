# ff-tool
ff-tool is a Python CLI tool for downloading desktop Firefox versions, 
as well as managing profiles and test prefs.  It is largely a glorified 
convenience wrapper we've written around these amazing tools/libraries:

* [mozdownload](https://github.com/mozilla/mozdownload)
* [mozprofile](https://github.com/mozilla/mozprofile)

NOTE:
If you plan on creating a tool of your own, please import the above libs 
directly in your script(s). This tool was designed for convenience of our 
team for testing Cloud Services and not intended to be used as a library.


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
_When not specified, ff will use defaults_

## Example(s)
```
$ ff -h
$ ff download -h
$ ff download -c nightly
```

## Launch browser, clean profile
* version: Nightly
* profile_name: <random>
```
$ ff run
```

## Launch browser, clean profile, specify profile name
* version: Nightly
* profile_name: my_cool_profile1

NOTE: if profile exists, we use it, if not we create a new one
with that name.

```
$ ff run -p my_cool_profile1
```
