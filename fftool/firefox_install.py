#!/usr/bin/env python

import os
import stat
from outlawg import Outlawg
from firefox_env_handler import IniHandler
from fftool import (
    DIR_TEMP_BROWSERS as BASE_DIR,
    DIR_CONFIGS,
    local
)

Log = Outlawg()
env = IniHandler()
env.load_os_config(DIR_CONFIGS)


def chmodx(path):
    mode = os.stat(path).st_mode
    os.chmod(path, mode | stat.S_IEXEC)


def install(channel):

    Log.header('INSTALL FIREFOX')

    install_dir = env.get(channel, 'PATH_FIREFOX_APP')
    filename = env.get(channel, 'DOWNLOAD_FILENAME')
    installer = os.path.join(BASE_DIR, filename)

    if IniHandler.is_linux():
        local('tar -jxf {0} && mv firefox {1}'.format(installer, install_dir))  # NOQA

    elif IniHandler.is_windows():
        chmodx(installer)
        local('"{0}" -ms'.format(installer))

        if channel == 'beta':
            # Since Beta and General Release channels install
            # to the same directory, install Beta first then
            # rename the directory.
            release_install_dir = env.config.get('release', 'PATH_FIREFOX_APP')
            local('mv "{0}" "{1}"'.format(release_install_dir, install_dir))

    elif IniHandler.is_mac():
        from hdiutil import extract_dmg

        app_src_filename = env.get(channel, "APP_SRC_FILENAME")
        app_dest_filename = env.get(channel, "APP_DEST_FILENAME")

        extract_dmg(installer, app_src_filename, app_dest_filename, channel)

    try:
        firefox_version = get_firefox_version(channel)
    except:
        print("ERROR: Install Failed - Aborting!")
        exit()

    Log.header("FIREFOX VERSION")
    print("Installed {0} ({1})".format(firefox_version, channel))


def get_firefox_version(channel):
    path_firefox_bin = env.get(channel, "PATH_FIREFOX_BIN_ENV")
    cmd = '"{0}" --version'.format(path_firefox_bin)
    return local(cmd)


def install_all():
    for channel in env.sections():
        install(channel)


def main():
    install_all()


if __name__ == '__main__':
    main()
