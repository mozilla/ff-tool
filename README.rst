======= 
ff-tool 
=======

|Build Status|

.. |Build Status| image:: https://travis-ci.org/rpappalax/ff-tool.svg?branch=dev
   :target: https://travis-ci.org/rpappalax/ff-tool

.. contents::

Summary
=======

ff-tool is a Python CLI tool we’ve created to facilitate browser testing
of cloud services. It is largely a convenience wrapper we’ve written
around these amazing tools/libraries (see note below):

-  `mozdownload <https://github.com/mozilla/mozdownload>`_
-  `mozprofile <https://github.com/mozilla/mozprofile>`_

Our typical use case is launching various Firefox browser versions with
a fresh profile and loading custom preferences. This tool enables us to
do this quickly with a 1-liner from the CLI.

Features
========

1. DownloadFirefox desktop versions (Nightly, Developer Edition, Beta,
   Release)
2. Manage profiles
3. Load test preferences

Notes
=====

If you plan on creating a tool of your own, please import the above lib
directly in your script(s). This tool was designed for convenience of
our team for testing Cloud Services and not intended to be used as a
library.

Profiles are stored in a temp directory by default which can be
overridden. Use caution if you specify your own profile directory as
profile cleanup functions can wipe out all profiles in your specified
directory.

**NOTE:** 

This tool is work in progress… USE AT YOUR OWN RISK!

Installation
============

**Pre-requisites**

-  Python >= 2.7 and virtualenv (Python 3 not yet supported)

**Windows Users**

-  ff-tool will work on Windows, but requires quite a bit of setup.
-  Also, installation behavior for the Firefox binary is different than
   for other OSes. In particular, ff-tool installs the Firefox binaries
   into a “\_temp” directory for all OSes (except Windows) to avoid
   clobbering your working browser. Unfortunately, the Windows installer
   forces installation into C:\\Program Files. Since both the release
   and Beta versions of Firefox install into the same place, you also
   run the risk of installing one over another.
-  Again, use at your own risk!

**Windows: Installing Cygwin**

-  Download and install: `Cygwin <https://cygwin.com/>`_
-  Right click on: c:\\\\cygwin64\\cygwin.bat
-  Run as administrator or you will suffer.
-  A number of dependencies must also be installed including: gcc, make,
   curl, pycrypto, python2, python-dev, etc.

**Build**

::

   $ make build
   $ source ./venv/bin/activate

**Cleanup**

::

   $ deactivate
   $ make clean

Run
===

*When not specified, ff will use defaults*

Help
====

::

   $ ff -h

Launch browser, clean profile
=============================

-  version: Nightly
-  profile\_name:

::

   $ ff

-  version: Developer Edition (aurora)
-  profile\_name:

::

   $ ff -c aurora

Launch browser, clean profile, specify profile name
===================================================

-  version: Nightly
-  profile\_name: my\_cool\_profile1

**NOTE:** If the specified profile exists, we use it, if not we create a
new one with that name.

::

   $ ff -p my_cool_profile1


Custom Browser Prefs
====================

Firefox provides the ability for a user to change preferences in
about:config. For testing and automation this can be cumbersome as it
usually involves many small steps.

As alternative, ff-tool provides a means for loading these prefs from a
root directory you specify via an environment variable.

Example:

::

   $ export PREFS_ROOT_DIR = '../services-test'

Custom prefs must be stored in the following directory/file structure:

You must also include a prefs.ini file which specifies the
environment(s) in which each pref set is used.

Example prefs.ini:

::

   [DEFAULT]
   pref_key = pref_value

   [dev]
   pref_key = pref_value

   [stage]
   pref_key = pref_value


Cloud Services (only)
=====================

Launch browser, clean profile, specify services-specific options...
-------------------------------------------------------------------

-  version: Beta
-  profile\_name: my\_cool\_profile1
-  product: loop-server
-  environment: stage
-  test-type: e2e-test

**NOTE:** If the specified profile exists, we use it, if not we create a
new one with that name.

::

   $ ff -c beta -p my_cool_profile1 -a loop-server -e stage -t e2e-test

