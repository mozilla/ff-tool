#!/usr/bin/env python

from fftool import PATH_PREFS_ROOT, Log
from arg_parser import arg_parser
from firefox_download import download
from firefox_profile import create_mozprofile, clean_profiles
from firefox_run import launch_firefox


def main():
    Log.header('FF-TOOL: download, install & launch Firefox!', 'XL', '=')
    options = arg_parser()

    if options.app and not PATH_PREFS_ROOT:
        Log.header("ERROR")
        print("Missing path to $PATH_PREFS_ROOT directory.")
        print("Please set the `PATH_PREFS_ROOT` environment variable and " +
              "try again.")
        exit()

    if (options.clean_profiles):
        clean_profiles()
        return

    # DOWNLOAD/INSTALL
    download(options.channel)

    # If user specified `--install-only`, then
    # download/install specified channel(s) and exit early.
    if (options.install_only):
        return

    # PROFILE
    if not options.no_profile:
        profile_path = create_mozprofile(
            options.profile,
            application=options.app,
            test_type=options.test_type,
            env=options.env
        )

    # LAUNCH
    if not options.no_launch:
        launch_firefox(profile_path, channel=options.channel)


if __name__ == '__main__':
    main()
