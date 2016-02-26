#!/usr/bin/env python

import os
import sys
from firefox_env_handler import IniHandler
from fabric.api import local


class FirefoxInstall(object):

    def __init__(self, config, archive_dir='temp'):

        #self.CACHE_FILE = 'cache.ini'
        self.out_dir = archive_dir
        #self.cache_path = os.path.join(self.out_dir, self.CACHE_FILE)
        #self.cache = IniHandler(self.cache_path)

        # Do some basic type checking on the `config` attribute.
        if isinstance(config, IniHandler):
            self.config = config

        elif isinstance(config, str):
            self.config = IniHandler()
            self.config.load_os_config(config)

        else:
            sys.exit('FirefoxInstall: Unexpected config data type')

    def install_all(self, force=False):
        IniHandler.banner('INSTALLING FIREFOXES')
        for channel in self.config.sections():
            self.install_channel(channel, force)

    def install_channel(self, channel, force=False):
        #was_cached = self.cache.config.getboolean('cached', channel)
        filename = self.config.get(channel, 'DOWNLOAD_FILENAME')
        install_dir = self.config.get(channel, 'PATH_FIREFOX_APP')
        installer = os.path.join('.', self.out_dir, filename)

        if force: # or not was_cached:
            print(('Installing {0}'.format(channel)))

            if IniHandler.is_linux():
                # TODO: Move to /opt/* and chmod file?
                # `tar -jxf firefox-beta.tar.gz -C ./beta --strip-components=1`?  # NOQA
                local('tar -jxf {0} && mv firefox {1}'.format(installer, install_dir))  # NOQA

            elif IniHandler.is_windows():
                local('{0} -ms'.format(installer))

                if channel == 'beta':
                    # Since Beta and General Release channels install
                    # to the same directory, install Beta first then
                    # rename the directory.
                    gr_install_dir = self.config.get('gr', 'PATH_FIREFOX_APP')
                    local('mv "{0}" "{1}"'.format(gr_install_dir, install_dir))

            elif IniHandler.is_mac():
                # TODO: Mount the DMG to /Volumes and copy to /Applications?

                cmd_hdiutil = 'hdiutil' #local('which hdiutil')

                name_browser = 'FirefoxNightly'
                path_temp = '_temp/browsers'
                path_temp_dmg = '_temp/browsers/_dmg_temp'

                path_browser_dmg = '{0}/{1}.dmg'.format(
                    path_temp, name_browser)

                path_browser_app = '{0}/{1}.app'.format(
                    path_temp_dmg, name_browser) 

                cmd = '{0} attach {1} -mountpoint {2}'.format(
                    cmd_hdiutil, path_browser_dmg, path_temp_dmg)
                local(cmd)

                cmd = 'cp -r {0} {1}'.format(
                    path_browser_app, path_temp) 
                local(cmd)

                cmd = '{0} detach {1}'.format(cmd_hdiutil, path_temp_dmg)
                local(cmd)

        else:
            print(('[{0}] was cached, skipping install.'.format(channel)))

        cmd = self.config.get(channel, 'PATH_FIREFOX_BIN_ENV')
        # local('"{0}" --version # {1}'.format(self.config.get(channel,
        #    'PATH_FIREFOX_BIN_ENV'), channel))
        local('"{0}" --version # {1}'.format(cmd, channel))


def main():
    ff_install = FirefoxInstall('./configs/')
    ff_install.install_all(True)


if __name__ == '__main__':
    main()
