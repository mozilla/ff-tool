from argparse import ArgumentParser

from fftool import CHANNELS, DEFAULT_CHANNEL


def arg_parser():
    parser = ArgumentParser(prog='ff')

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
        '-a',
        '--app',
        help="Name of the application to test (ie: loop-server)."
    )

    parser.add_argument(
        '-t',
        '--test-type',
        help="Name of the test-type (ie: e2e-test, stack-check)."
    )

    parser.add_argument(
        '-f',
        '--prefs',
        help='prefs to specify (i.e. dev, stage, prod) or \
              specify multiple prefs contatenated with a "+" \
              (i.e. stage+mozfull, pre-prod+mozstd, etc.)'
    )

    parser.add_argument(
        '-l',
        '--logging',
        action='store_true',
        help="Output Firefox logging."
    )

    parser.add_argument(
        '-n',
        '--nspr-log-modules',
        help="Output Firefox NSPR logging. \
              https://developer.mozilla.org/docs/Mozilla/Projects/NSPR/Reference/NSPR_LOG_MODULES"  # noqa
    )

    parser.add_argument(
        '--install-only',
        action='store_true',
        help="Whether or not to just download/install Firefox version(s), \
              or also create a profile and launch a browser."
    )

    parser.add_argument(
        '--clean-profiles',
        action='store_true',
        help="Delete all the fftool.* profile directories in the _temp/profiles\
              directory"
    )

    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help="Print ff-tool version, then quit."
    )

    return parser.parse_args()
