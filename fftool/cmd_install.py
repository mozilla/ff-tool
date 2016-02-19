"""
ff-tool <install> specific arguments...
"""


class cmd_install():
    def cmd(self, args):
        print('Installing Firefox... [channel: {0}]'.format(args.channel))

    def __init__(self, subparsers, CHANNELS, DEFAULT_CHANNEL):
        install = subparsers.add_parser('install', help='<install> command help')
        install.add_argument(
            '-c',
            '--channel',
            choices=CHANNELS,
            default=DEFAULT_CHANNEL,
            type=str,
            help='Install a specific Firefox channel.'
        )
        install.set_defaults(func=self.cmd)
