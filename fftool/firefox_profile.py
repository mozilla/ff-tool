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
from tempfile import mkdtemp
from mozprofile import Profile, Preferences
from outlawg import Outlawg
from fftool import DIR_TEMP_PROFILES as BASE_PROFILE_DIR


try:
    import configparser  # Python 3
except:
    import ConfigParser as configparser  # Python 2

PATH_PROJECT = os.path.abspath('.')
FILE_PREFS = 'prefs.ini'

config = configparser.ConfigParser()
out = Outlawg()


def prefs_paths(application, test_type, env='stage'):
    path_global = os.path.join(PATH_PROJECT, 'configs', FILE_PREFS)
    valid_paths = [path_global]

    if application:
        path_app_dir = os.path.join(PATH_PROJECT, application)

        path_app = os.path.join(path_app_dir, FILE_PREFS)
        if os.path.exists(path_app):
            config.read(path_app)
            # Make sure the specified INI file has the specified section.
            if config.has_section(env):
                valid_paths.append(path_app + ":" + env)
            else:
                valid_paths.append(path_app)

        if test_type:
            path_app_test_type = os.path.join(
                path_app_dir, test_type, FILE_PREFS)
            if os.path.exists(path_app_test_type):
                config.read(path_app_test_type)
                if config.has_section(env):
                    valid_paths.append(path_app_test_type + ":" + env)
                else:
                    valid_paths.append(path_app_test_type)

    return valid_paths


def create_mozprofile(profile_dir, application=None, test_type=None, env=None):
    # Ensure that the base `_temp/profiles/` directory exists before trying to
    # create a nested directory.
    if not os.path.exists(BASE_PROFILE_DIR):
        os.mkdir(BASE_PROFILE_DIR)

    if not profile_dir:
        full_profile_dir = mkdtemp(
            dir=BASE_PROFILE_DIR,
            prefix="fftool.",
            suffix=""
        )

    else:
        full_profile_dir = os.path.join(BASE_PROFILE_DIR, profile_dir)

        if os.path.exists(full_profile_dir):
            msg = "WARNING: Profile '{0}' already exists. Merging configs."
            out.header(msg.format(full_profile_dir), 'XL', '-')

    prefs = Preferences()

    for path in prefs_paths(application, test_type):
        prefs.add_file(path)

    # Add the `fftool.profile.name` pref so we can go to about:config and see
    # what our current profile is.
    prefs.add([("fftool.profile.name", full_profile_dir)])

    profile = Profile(
        profile=full_profile_dir, restore=False, preferences=prefs())

    # TODO: Return the path to the profile, or the profile object?
    return profile.profile  # this is the path to the created profile
