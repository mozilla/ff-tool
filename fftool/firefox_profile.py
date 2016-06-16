"""This module creates a Firefox Profile by concatenating the
preferences files specified by --prefs-dirs, like so:
- ./_utils/prefs.ini
- ./<application>/prefs.ini
- ./<application>/<test_type>/prefs.ini

The profile is then created using the specified name and
saved to the ../.cache/ directory.
"""

import os
import shutil
import ConfigParser as configparser
from tempfile import mkdtemp
from outlawg import Outlawg
from mozprofile import Profile, Preferences
from ini_handler import IniHandler
from fftool import (
    DIR_TEMP_PROFILES as BASE_PROFILE_DIR,
    DIR_CONFIGS,
    PATH_PREFS_ROOT,
    FILE_PREFS,
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


def prefs_paths(prefs_dirs):
    # we'll always use seed with this global set of testing prefs
    path_global = os.path.join(PATH_PREFS_GLOBAL, DIR_CONFIGS, FILE_PREFS)
    valid_paths = [path_global]

    # user can specify prefs for a given file like so:
    # -d my/path/here
    # or
    # -d my/path/here:section1+section2+section3
    # (in this case we'll only grab specified sections)
    # We'll also convert this to format mozprofile can work with:
    # /Abs/path/my/path/here:section1
    # /Abs/path/my/path/here:section2
    # /Abs/path/my/path/here:section3

    for prefs_dir in prefs_dirs:
        prefs_dir_chunks = prefs_dir.split(':')
        path_pref_file = os.path.join(
            PATH_PREFS_ROOT,
            prefs_dir_chunks[0],
            FILE_PREFS
        )
        # TODO:
        # add in valid_paths_list checker
        if ':' in prefs_dir:
            if '+' in prefs_dir:
                sections = prefs_dir_chunks[1].split('+')
            else:
                sections = [prefs_dir_chunks[1]]

            for section in sections:
                path_tmp = '{0}:{1}'.format(path_pref_file, section)
                valid_paths.append(path_tmp)
        else:
            valid_paths.append(path_pref_file)

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


def create_mozprofile(profile_dir, prefs_dirs=None, env=None):
    # Ensure base `.cache/profiles/` dir exists before trying to
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

    if prefs_dirs:
        for path in prefs_paths(prefs_dirs):
            print('PREFS.ADD_FILE(PATH): ' + path)
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
