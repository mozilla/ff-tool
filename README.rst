=======
ff-tool
=======

|Build Status|

.. |Build Status| image:: https://travis-ci.org/mozilla/ff-tool.svg?branch=dev
   :target: https://travis-ci.org/mozilla/ff-tool?branch=dev

.. contents::

Summary
=======

ff-tool is a Python CLI tool we’ve created to facilitate browser testing
of cloud services. It is largely a convenience wrapper we’ve written
around these amazing tools/libraries (see note below):

-  `mozdownload <https://github.com/mozilla/mozdownload>`_
-  `mozprofile <http://mozbase.readthedocs.io/en/latest/mozprofile.html>`_

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

Launch browser, clean profile, specify profile name
===================================================

-  version: Nightly
-  profile\_name: my\_cool\_profile1

**NOTE:** If the specified profile exists, we use it, if not we create a
new one with that name.

::

   $ ff -p my_cool_profile1


Preinstalling Profile Add-ons
=============================

Fully qualified URL to an add-on XPI to install in profile.
Firefox/mozprofile provides the ability to specify zero or more add-ons to
preinstall into a profile.

Example:

::

   $ ff -c nightly -p my-profile-name -a https://moz-activity-streams-dev.s3.amazonaws.com/dist/activity-streams-latest.xpi --addon https://testpilot.firefox.com/files/pageshot/pageshot-0.1.201609272025.xpi



Custom Browser Prefs
====================

Firefox provides the ability for a user to change preferences in
about:config. For testing and automation this can be cumbersome as it
usually involves many small steps.

As alternative, ff-tool provides a means for loading these prefs from a
root directory you specify via an environment variable.

Example:

::

   $ export PATH_PREFS_ROOT = '../services-test'

Custom prefs must be stored in the following directory/file structure:

You must also include a prefs.ini file which specifies the
pref(s) in which each pref set is used. This is especially useful for
defining things like pref sets you want to define for a specific test
environment (example: dev, stage, pre-prod, prod).

You can specify one pref or multiple prefs by concatenating them
with a "+" sign.  i.e. stage or  stage+fruits

Some prefs (like test environments) would only make sense specifying
one of those at a time.  For example, you wouldn't specify: dev+stage+prod,
but you could specify: prod+fruits+vegetables

Example prefs.ini:

::

   [DEFAULT]
   pref_key = pref_value

   [dev]
   pref_key = pref_value

   [stage]
   pref_key = pref_value

   [fruits]
   banana = yellow

   [vegetables]
   asparagus = green


Offline use
=====================

ff-tool has a --no-download option.

::

  $ ff --no-download


This may may be useful if wifi is down / internet unavailable or you simply want
to use ff-tool with a cached version of Firefox.

NOTE:
The --no-download option will not work if you don't have a cached version of firefox
in your _temp (cache) folder.


Cloud Services (only)
=====================

Launch browser, clean profile, specify services-specific options...
-------------------------------------------------------------------

-  version: Beta
-  profile\_name: my\_cool\_profile1
-  product: loop-server
-  test-type: e2e-test
-  prefs: stage

**NOTE:** If the specified profile exists, we use it, if not we create a
new one with that name.

::

   $ ff -c beta -p my_cool_profile1 -d loop-server/e2e-test:stage
   $ ff -c nightly -p my_cool_profile2 -d shavar/e2e-test:stage+moztestpub
