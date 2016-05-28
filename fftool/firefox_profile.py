"""This module creates a Firefox Profile by concatenating the
following preferences files:
- ./_utils/prefs.ini
- ./<application>/prefs.ini
- ./<application>/<test_type>/prefs.ini

The profile is then created using the specified name and
saved to the ../_temp/ directory.
"""

import os
import shutil
import ConfigParser as configparser
from tempfile import mkdtemp
from outlawg import Outlawg
from mozprofile import Profile, Preferences
from firefox_env_handler import IniHandler
from fftool import (
    DIR_TEMP_PROFILES as BASE_PROFILE_DIR,
    DIR_CONFIGS,
    PATH_PREFS_ROOT,
    FILE_PREFS,
    PLUS
)


PATH_PREFS_GLOBAL = os.path.abspath('.')

config = configparser.ConfigParser()
Log = Outlawg()


def valid_path_list(prefs, valid_paths, path_app):
    if os.path.exists(path_app):
        config.read(path_app)
        # Make sure the specified INI file has the specified section.

        for env in prefs:
            if config.has_section(env):
                valid_paths.append(path_app + ":" + env)
            else:
                valid_paths.append(path_app)
    return valid_paths


def prefs_paths(application, test_type, option_prefs=''):
    path_global = os.path.join(PATH_PREFS_GLOBAL, DIR_CONFIGS, FILE_PREFS)
    valid_paths = [path_global]

    # convert prefs option to an iterable
    if option_prefs is None:
        option_prefs = ''
    prefs = option_prefs.split(PLUS)

    if application:
        path_app_dir = os.path.join(PATH_PREFS_ROOT, application)

        path_app = os.path.join(path_app_dir, FILE_PREFS)

        valid_paths = valid_path_list(prefs, valid_paths, path_app)

        if test_type:
            path_app_test_type = os.path.join(
                path_app_dir, test_type, FILE_PREFS)

            valid_paths = valid_path_list(prefs, valid_paths,
                                          path_app_test_type)

    return valid_paths


def clean_profiles():
    try:
        os.remove(os.path.join(BASE_PROFILE_DIR, "profiles.ini"))
    except:
        pass

    if IniHandler.is_windows():
        profile_dir = os.path.join(BASE_PROFILE_DIR, "Profiles")
    else:
        profile_dir = BASE_PROFILE_DIR

    shutil.rmtree(profile_dir, True)


def create_mozprofile(profile_dir, application=None, test_type=None, env=None):

    # Ensure base `_temp/profiles/` dir exists before trying to
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
            Log.header(msg.format(full_profile_dir), 'XL', '-')

    prefs = Preferences()

    for path in prefs_paths(application, test_type, env):
        prefs.add_file(path)

    # Add custom user pref: `fftool.profile.name`
    # so we can go to about:config and verify our current profile.
    prefs.add([("fftool.profile.name", full_profile_dir)])

    profile = Profile(
        profile=full_profile_dir, restore=False, preferences=prefs())

    Log.header("USER CONFIGS")
    print("Launching browser with the following user configs:")
    print(profile.summary())

    return full_profile_dir
