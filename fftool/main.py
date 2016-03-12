#!/usr/bin/env python

import argparse

from firefox_download import download
from firefox_profile import create_mozprofile
from firefox_run import launch_firefox

CHANNELS = ['release',
            'beta',
            'aurora',
            'nightly',
            'ALL']
DEFAULT_CHANNEL = 'nightly'


def main():
    parser = argparse.ArgumentParser(prog='ff')

    """
    Global arguments...
    """

    parser.add_argument(
        '-c',
        '--channel',
        choices=CHANNELS,
        default=DEFAULT_CHANNEL,
        help='A specific Firefox channel.'
    )

    # Assume existing profile will be overwritten.
    parser.add_argument(
        '-p',
        '--profile',
        help='Name of the Firefox profile to create/use.'
    )

    parser.add_argument(
        '-e',
        '--env',
        help='Development environment to use (ie: dev, stage, prod).'
    )

    parser.add_argument(
        '-t',
        '--test-type',
        help="Name of the test-type (ie: e2e-test, stack-check)."
    )

    parser.add_argument(
        '-a',
        '--app',
        help="Name of the application to test (ie: loop-server)."
    )

    parser.add_argument(
        '--no-launch',
        action='store_true',
        help="Whether or not to launch a Firefox instance."
    )

    parser.add_argument(
        '--no-profile',
        action='store_true',
        help="Whether to create a profile. This is used for the daily refresh job."
    )

    options = parser.parse_args()

    # DOWNLOAD/INSTALL
    download(options.channel)

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
