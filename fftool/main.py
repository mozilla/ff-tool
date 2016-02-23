#!/usr/bin/env python

import argparse

from cmd import CMDDownload, CMDInstall, CMDUninstall, CMDProfile

CHANNELS = ['gr', 'release', 'stable',
            'beta',
            'aurora', 'devedition', 'developeredition',
            'nightly',
            'ALL']
DEFAULT_CHANNEL = 'nightly'


def get_channel(channel):
    # Remap some channel names.
    channels = {
        'release': 'gr',
        'stable': 'gr',
        'devedition': 'aurora',
        'developeredition': 'aurora'
    }

    if channel in channels:
        return channels[channel]

    return channel


def main():
    parser = argparse.ArgumentParser(prog='ff')
    subparsers = parser.add_subparsers(help='commands', dest='command')

    """
    Global arguments...
    """
    # parser.add_argument('--foo', action='store_true', help='foo help')

    CMDDownload(subparsers, CHANNELS, DEFAULT_CHANNEL)
    CMDInstall(subparsers, CHANNELS, DEFAULT_CHANNEL)
    CMDProfile(subparsers)
    CMDUninstall(subparsers, CHANNELS, DEFAULT_CHANNEL)

    options = parser.parse_args()
    if "channel" in options:
        options.channel = get_channel(options.channel)

    options.func(options)


if __name__ == '__main__':
    main()
