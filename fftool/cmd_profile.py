"""
ff-tool <profile> specific arguments...
"""


class cmd_profile():
    def cmd(self, args):
        if args.create:
            print('Creating Firefox profile... [name: {0}]'.format(args.create))

        if args.delete:
            print('Deleting Firefox profile... [name: {0}]'.format(args.delete))

    def __init__(self, subparsers):
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
        profile.set_defaults(func=self.cmd)
