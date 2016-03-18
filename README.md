# ff-tool

[![Build Status](https://travis-ci.org/rpappalax/ff-tool.svg?branch=master)](https://travis-ci.org/rpappalax/ff-tool)

## Summary

ff-tool is a Python CLI tool we've created to facilitate browser testing of
cloud services. It is largely a convenience wrapper we've written around
these amazing tools/libraries (see note below):

- [mozdownload](https://github.com/mozilla/mozdownload)
- [mozprofile](https://github.com/mozilla/mozprofile)

Our typical use case is launching various Firefox browser versions with a
fresh profile and loading custom preferences. This tool enables us to do this
quickly with a 1-liner from the CLI.

## Features

1. DownloadFirefox desktop versions (Nightly, Developer Edition, Beta, Release)
2. Manage profiles
3. Load test preferences

## Notes

If you plan on creating a tool of your own, please import the above lib
directly in your script(s). This tool was designed for convenience of our
team for testing Cloud Services and not intended to be used as a library.

Profiles are stored in a temp directory by default which can be overridden.
Use caution if you specify your own profile directory as profile cleanup
functions can wipe out all profiles in your specified directory.


:bangbang: _**NOTE:** This tool is work in progress...  DO NOT USE_ :bangbang:


## Installation

### Pre-requisites

**NOTE:** ff-tool requires you have Python 2.7 (not Python 3.x) and virtualenv installed.
Windows users must have Cygwin installed. If using Cygwin, you must run it as administrator.

1. Right click on c:\cygwin64\cygwin.bat
2. Run as administrator

**NOTE:** You will also need to run the Cygwin setup file to install a number of modules including: gcc, make, curl, pycrypto, python2, python-dev, etc.

### Build
```sh
$ make build
$ source ./venv/bin/activate
```

### Cleanup
```sh
$ deactivate
$ make clean
```

## Run
_When not specified, ff will use defaults_

## Help
```sh
$ ff -h
```

## Launch browser, clean profile

* version: Nightly
* profile_name: \<random\>
```sh
$ ff
```

* version: Developer Edition (aurora)
* profile_name: \<random\>
```sh
$ ff -c aurora
```

## Launch browser, clean profile, specify profile name

* version: Nightly
* profile_name: my_cool_profile1

**NOTE:** If the specified profile exists, we use it, if not we create a new one
with that name.

```sh
$ ff -p my_cool_profile1
```

# Custom Browser Prefs

Firefox provides the ability for a user to change preferences in about:config.
For testing and automation this can be cumbersome as it usually involves many 
small steps.

As alternative, ff-tool provides a means for loading these prefs from a root 
directory you specify via an environment variable.

Example:
```sh
$ export PREFS_ROOT_DIR = '../services-test'
```

Custom prefs must be stored in the following directory/file structure:
<prefs root dir>/<product name>/<test type>

You must also include a prefs.ini file which specifies the environment(s)
in which each pref set is used.

Example prefs.ini:
```sh
[DEFAULT]
pref_key = pref_value

[dev]
pref_key = pref_value

[stage]
pref_key = pref_value
```

# Cloud Services (only)


## Launch browser, clean profile, specify services-specific options...

* version: Beta
* profile_name: my_cool_profile1
* product: loop-server
* environment: stage
* test-type: e2e-test

**NOTE:** If the specified profile exists, we use it, if not we create a new one
with that name.

```sh
$ ff -c beta -p my_cool_profile1 -a loop-server -e stage -t e2e-test
```

## Download all browsers, but don't create a profile or launch any browsers...

**NOTE:** This is useful for our daily refresh task where we make sure we have
the latest browsers installed.

* version: all
* profile_name: none

```sh
$ ff -c ALL --install-only
```
