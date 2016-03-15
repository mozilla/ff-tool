#!/usr/bin/env python

import os
from firefox_env_handler import IniHandler
from fabric.api import local
from outlawg import Outlawg

env = IniHandler()
env.load_os_config('configs')

out = Outlawg()


def install(channel):
    if channel == 'ALL':
        install_all()
        return

    # filename = env.get(channel, 'DOWNLOAD_FILENAME')
    install_dir = env.get(channel, 'PATH_FIREFOX_APP')
    print(IniHandler.get_os())

    if IniHandler.is_linux():
        local('tar -jxf {0} && mv firefox {1}'.format(installer, install_dir))  # NOQA

    elif IniHandler.get_os() == 'cygwin':
        # TODO: this needs improvement
        filename = env.get(channel, 'DOWNLOAD_FILENAME')
        installer = os.path.join('.', '_temp', 'browsers', filename)
        print('INSTALLER:' + installer)
        local('/usr/bin/chmod +x {0}'.format(installer))
        local('{0} -ms'.format(installer))

        if channel == 'beta':
            # Since Beta and General Release channels install
            # to the same directory, install Beta first then
            # rename the directory.
            gr_install_dir = self.config.get('gr', 'PATH_FIREFOX_APP')
            local('mv "{0}" "{1}"'.format(gr_install_dir, install_dir))

    elif IniHandler.is_mac():
        from hdiutil import extract_dmg

        app_src_filename = env.get(channel, "APP_SRC_FILENAME")
        app_dest_filename = env.get(channel, "APP_DEST_FILENAME")
        dmg_filename = env.get(channel, "DOWNLOAD_FILENAME")
        dmg_dirname = os.path.join('_temp', 'browsers', dmg_filename)

        extract_dmg(dmg_dirname, app_src_filename, app_dest_filename, channel)

    firefox_version = get_firefox_version(channel)
    out.header("Installed {0} ({1})".format(firefox_version, channel))


def get_firefox_version(channel):
    path_firefox_bin = env.get(channel, "PATH_FIREFOX_BIN_ENV")
    cmd = "{0} --version".format(path_firefox_bin)
    return local(cmd, capture=True)


def install_all():
    for channel in env.sections():
        install(channel)


def main():
    install_all()


if __name__ == '__main__':
    main()
