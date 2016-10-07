from argparse import ArgumentParser

from fftool import CHANNELS, DEFAULT_CHANNEL


def arg_parser():
    parser = ArgumentParser(prog='ff')

    parser.add_argument(
        '-a',
        '--addon',
        action='append',
        help='Fully qualified URL to an add-on XPI to install in profile.'
    )

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
        '-d',
        '--prefs-dirs',
        action='append',
        help="Relative path(s) to prefs file(s) - OK to specify multiple. \
              NOTE: pref file must be called: prefs.ini"
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
        '--no-download',
        action='store_true',
        help="Use cached Firefox (no download)."
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
        help="Delete all the fftool.* profile directories in the .cache/profiles\
              directory"
    )

    parser.add_argument(
        '-v',
        '--version',
        action='store_true',
        help="Print ff-tool version, then quit."
    )

    return parser.parse_args()
