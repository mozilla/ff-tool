#!/usr/bin/env python

from fftool import DEFAULT_CHANNEL, PATH_PREFS_ROOT, Log
from ff_cli import ff_cli
from firefox_download import download
from firefox_profile import create_mozprofile
from firefox_run import launch_firefox


def main():
    options = ff_cli()

    # If the user is trying to create application specific configs but didn't
    # specify their `$PATH_PREFS_ROOT` environment variable, exit early.
    if options.app and not PATH_PREFS_ROOT:
        Log.header("ERROR")
        print("Missing path to $PATH_PREFS_ROOT directory.")
        print("Please set the `PATH_PREFS_ROOT` environment variable and " +
              "try again.")
        exit()

    # DOWNLOAD/INSTALL
    download(options.channel)

    # If user specified `--install-only`, then just download/install specified
    # channel(s) and exit early.
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
    # If we downloaded "ALL" browsers/channels, override the specified channel
    # with the default channel so we only launch one browser.
    if options.channel.upper() == 'ALL':
        options.channel = DEFAULT_CHANNEL

    if not options.no_launch:
        launch_firefox(profile_path, channel=options.channel)


if __name__ == '__main__':
    main()
