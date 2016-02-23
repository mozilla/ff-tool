"""
This module uses Fabric API to generate a Firefox Profile by concatenating the
following preferences files:
- ./_utils/prefs.ini
- ./<application>/prefs.ini
- ./<application>/<test_type>/prefs.ini

The profile is then created using the specified name and saved to the ../_temp/
directory.
"""

import os
import shutil

try:
    import configparser  # Python 3
except:
    import ConfigParser as configparser  # Python 2

from fabric.api import local  # It looks like Fabric may only support Python 2.

PATH_PROJECT = os.path.abspath('.')
PATH_TEMP = os.path.join(PATH_PROJECT, '_temp', 'profiles')
FILE_PREFS = 'prefs.ini'

config = configparser.ConfigParser()


def prefs_paths(application, test_type, env='stage'):
    path_global = os.path.join(PATH_PROJECT, 'configs', FILE_PREFS)
    path_app_dir = os.path.join(PATH_PROJECT, application)
    path_app = os.path.join(path_app_dir, FILE_PREFS)
    path_app_test_type = os.path.join(path_app_dir, test_type, FILE_PREFS)

    valid_paths = [path_global]

    if os.path.exists(path_app):
        config.read(path_app)
        # Make sure the specified INI file has the specified section.
        if config.has_section(env):
            valid_paths.append(path_app + ":" + env)

    if os.path.exists(path_app_test_type):
        config.read(path_app_test_type)
        if config.has_section(env):
            valid_paths.append(path_app_test_type + ":" + env)

    return valid_paths


def create_mozprofile(application, test_type, env, profile_dir):
    full_profile_dir = os.path.join(PATH_TEMP, profile_dir)

    # If temp profile already exists, kill it so it doesn't merge unexpectedly.
    if os.path.exists(full_profile_dir):
        print("Deleting existing profile... {0}".format(full_profile_dir))
        shutil.rmtree(full_profile_dir)

    cmd = [
        'mozprofile',
        '--profile={0}'.format(full_profile_dir)
    ]
    for path in prefs_paths(application, test_type, env):
        cmd.append("--preferences=" + path)

    local(" ".join(cmd))
