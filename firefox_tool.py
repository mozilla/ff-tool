"""firefox test tool helper script"""
import glob
import configargparse


def _parse_args():
    """Parses out args for CLI"""
    parser = configargparse.ArgumentParser(
        description='cross-platform CLI tool for installing firefox and managing profiles')
    parser.add_argument('-i', '--install',
                        help='install firefox version (release, beta, aurora, nightly',
                        default='nightly',
                        type=str)
    parser.add_argument('-u', '--uninstall',
                        help='install firefox version (release, beta, aurora, nightly, ALL',
                        type=str)
    parser.add_argument('-p', '--create-profile',
                        help='create new profile (indicate name)',
                        type=str)
    parser.add_argument('-d', '--delete-profile',
                        help='delete profile (indicate name)',
                        type=str)
    parser.add_argument('-s', '--set-profile-path',
                        help='-s <path to profile>',
                        default='<put OS-specific default path here??>',
                        type=str)

    args = parser.parse_args()
    return args, parser


def main():
    """Main entrypoint for CLI"""

    args, parser = _parse_args()

    print('INSTALL: {0}'.format(args.install))
    print('UNINSTALL: {0}'.format(args.uninstall))
    print('CREATE PROFILE: {0}'.format(args.create_profile))
    print('DELETE PROFILE: {0}'.format(args.delete_profile))
    print('SET PROFILE PATH: {0}'.format(args.set_profile_path))


if __name__ == '__main__':
    main()
