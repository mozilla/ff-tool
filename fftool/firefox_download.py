"""
Module to download OS-specific versions of Firefox:
1. General Release (gr)
2. Beta (beta)
3. Developer Edition (aurora)
4. Nightly (nightly)
"""

import os

from firefox_env_handler import IniHandler
from mozdownload import FactoryScraper


BASE_DIR = os.path.join('_temp', 'browsers')
CONFIG_CHANNELS = os.path.join('configs', 'channels.ini')

try:
    import configparser  # Python 3
except:
    import ConfigParser as configparser  # Python 2

config = configparser.ConfigParser()
config.read(CONFIG_CHANNELS)
env = IniHandler()
env.load_os_config('configs')


def set_channel(channel):
    ch_type = config.get(channel, 'type')
    ch_version = config.get(channel, 'version')
    ch_branch = config.get(channel, 'branch')
    return ch_type, ch_version, ch_branch


def download(channel):
    if channel == 'ALL':
        download_all()
        return

    t, v, b = set_channel(channel)
    download_filename = env.get(channel, 'DOWNLOAD_FILENAME')
    download_path = os.path.join(BASE_DIR, download_filename)
    scraper = FactoryScraper(
        t,
        version=v,
        branch=b,
        destination=download_path
    )

    print("Downloading {0} to {1}".format(channel, download_path))
    scraper.download()


def download_all():
    for channel in config.sections():
        download(channel)


def main():
    download_all()


if __name__ == '__main__':
    main()
