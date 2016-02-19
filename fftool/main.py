#!/usr/bin/env python

import argparse

CHANNELS = ['gr', 'beta', 'aurora', 'nightly', 'ALL']
DEFAULT_CHANNEL = 'nightly'

parser = argparse.ArgumentParser(prog='ff-tool')
subparsers = parser.add_subparsers(help='commands', dest='command')

"""
Global arguments...
"""
# parser.add_argument('--foo', action='store_true', help='foo help')


"""
ff-tool <download> specific arguments...
"""
download = subparsers.add_parser('download', help='<download> command help')
download.add_argument(
    '-c',
    '--channel',
    choices=CHANNELS,
    default=DEFAULT_CHANNEL,
    type=str,
    help='Download a specific Firefox channel via mozdownload.'
)

"""
ff-tool <install> specific arguments...
"""
install = subparsers.add_parser('install', help='<install> command help')
install.add_argument(
    '-c',
    '--channel',
    choices=CHANNELS,
    default=DEFAULT_CHANNEL,
    type=str,
    help='Install a specific Firefox channel.'
)

"""
ff-tool <profile> specific arguments...
"""
profile = subparsers.add_parser('profile', help='<profile> command help')
profile.add_argument(
    '-c',
    '--create',
    type=str,
    help='Create a new Firefox profile with the specified name.'
)
profile.add_argument(
    '-d',
    '--delete',
    type=str,
    help='Delete the specified Firefox profile.'
)

"""
ff-tool <uninstall> specific arguments...
"""
uninstall = subparsers.add_parser('uninstall', help='<uninstall> command help')
uninstall.add_argument(
    '-c',
    '--channel',
    choices=CHANNELS,
    default=DEFAULT_CHANNEL,
    type=str,
    help='Uninstall a specific Firefox channel.'
)

options = parser.parse_args()

if options.command == 'download':
    print("Downloading Firefox... [channel: {0}]".format(options.channel))

elif options.command == 'install':
    print("Installing Firefox... [channel: {0}]".format(options.channel))

elif options.command == 'profile':
    if options.create:
        print("Creating Firefox profile... [name: {0}]".format(options.create))

    if options.delete:
        print("Deleting Firefox profile... [name: {0}]".format(options.delete))

elif options.command == 'uninstall':
    print("Uninstalling Firefox... [channel: {0}]".format(options.channel))

print(options)
