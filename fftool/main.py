#!/usr/bin/env python

import argparse

from firefox_download import download


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
        type=str,
        help='A specific Firefox channel.'
    )

    # Assume existing profile will be overwritten.
    parser.add_argument(
        '-p',
        '--profile',
        help='Name of the Firefox to create/use.'
    )

    parser.add_argument(
        '-e',
        '--env',
        help='Developmenent environment to use (ie: dev, stage, prod).'
    )

    parser.add_argument(
        '-t',
        '--test-type',
        help="TODO: (ie: e2e-test, stack-check)."
    )

    parser.add_argument(
        '-a',
        '--app',
        help="Name of the application to test (ie: loop-server)."
    )

    parser.add_argument(
        '--no-launch',
        action='store_true',
        help="TODO:"
    )

    """
    TODO-this:
    parser.add_argument(
        '--no-profile',
        help="TODO:"
    )
    """

    options = parser.parse_args()


    # INSTALL
    print("Installing...")
    download(options.channel)

    # PROFILE
    print("Creating profile...")

    # LAUNCH
    if not options.no_launch:
        print("Launching!")



    if not options.env:
        print("Unknown env")
    else:
        print("Load settings for env: {0}".format(options.env))


    if not options.profile:
        print("Create random profile")
    else:
        print("Create new profile with name {0}".format(options.profile))


if __name__ == '__main__':
    main()
