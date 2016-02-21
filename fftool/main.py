#!/usr/bin/env python

import argparse

from cmd_download import cmd_download
from cmd_install import cmd_install
from cmd_profile import cmd_profile
from cmd_uninstall import cmd_uninstall

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


parser = argparse.ArgumentParser(prog='ff')
subparsers = parser.add_subparsers(help='commands', dest='command')

"""
Global arguments...
"""
# parser.add_argument('--foo', action='store_true', help='foo help')

download = cmd_download(subparsers, CHANNELS, DEFAULT_CHANNEL)
install = cmd_install(subparsers, CHANNELS, DEFAULT_CHANNEL)
profile = cmd_profile(subparsers)
uninstall = cmd_uninstall(subparsers, CHANNELS, DEFAULT_CHANNEL)

options = parser.parse_args()
if "channel" in options:
    options.channel = get_channel(options.channel)

options.func(options)
