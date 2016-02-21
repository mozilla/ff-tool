"""
ff-tool <download> specific arguments...
"""

from firefox_download import download


class cmd_download():
    def cmd(self, args):
        print('Downloading Firefox... [channel: {0}]'.format(args.channel))

        download(args.channel)

    def __init__(self, subparsers, CHANNELS, DEFAULT_CHANNEL):
        download = subparsers.add_parser('download', help='<download> command help')
        download.add_argument(
            '-c',
            '--channel',
            choices=CHANNELS,
            default=DEFAULT_CHANNEL,
            type=str,
            help='Download a specific Firefox channel via mozdownload.'
        )
        download.set_defaults(func=self.cmd)
