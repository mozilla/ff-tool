"""
ff-tool <uninstall> specific arguments...
"""


class cmd_uninstall():
    def cmd(self, args):
        print('Uninstalling Firefox... [channel: {0}]'.format(args.channel))

    def __init__(self, subparsers, CHANNELS, DEFAULT_CHANNEL):
        uninstall = subparsers.add_parser('uninstall', help='<uninstall> command help')
        uninstall.add_argument(
            '-c',
            '--channel',
            choices=CHANNELS,
            default=DEFAULT_CHANNEL,
            type=str,
            help='Uninstall a specific Firefox channel.'
        )
        uninstall.set_defaults(func=self.cmd)
