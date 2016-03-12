"""
Module to download OS-specific versions of Firefox:
1. General Release (gr)
2. Beta (beta)
3. Developer Edition (aurora)
4. Nightly (nightly)
"""

import os
import time

from firefox_install import install, get_firefox_version
from firefox_env_handler import IniHandler
from mozdownload import FactoryScraper
from outlawg import Outlawg

try:
    import configparser  # Python 3
except:
    import ConfigParser as configparser  # Python 2


BASE_DIR = os.path.join('_temp', 'browsers')
CONFIG_CHANNELS = os.path.join('configs', 'channels.ini')
SCRIPT_START_TIME = time.time()

config = configparser.ConfigParser()
config.read(CONFIG_CHANNELS)

env = IniHandler()
env.load_os_config('configs')

out = Outlawg()


def replace_ext(filename, ext):
    """
    Takes a filename, and changes it's extension.
    """
    basename = os.path.splitext(filename)[0]
    args = {"basename": basename, "ext": ext}
    return "{basename}.{ext}".format(**args)


def modification_date(filename):
    return os.path.getmtime(filename)


def download(channel):
    if channel == 'ALL':
        download_all()
        return

    ch_type = config.get(channel, 'type')
    ch_version = config.get(channel, 'version')
    ch_branch = config.get(channel, 'branch')

    download_filename = env.get(channel, 'DOWNLOAD_FILENAME')
    download_path = os.path.join(BASE_DIR, download_filename)
    scraper = FactoryScraper(
        ch_type,
        version=ch_version,
        branch=ch_branch,
        destination=download_path
    )

    args = {"channel": channel, "download_path": download_path}
    print("Downloading {channel} to {download_path}".format(**args))
    scraper.download()

    is_recent_file = modification_date(download_path) > SCRIPT_START_TIME
    firefox_bin = env.get(channel, 'PATH_FIREFOX_BIN_ENV')

    # If the *.dmg file was downloaded recently, or we don't have the *.app
    # file installed, install the current Firefox channel.
    if is_recent_file or not os.path.exists(firefox_bin):
        install(channel)

    else:
        firefox_version = get_firefox_version(channel)
        args = {"channel": channel, "version": firefox_version}
        msg = "You have the latest version of {channel} installed ({version})."
        out.header(msg.format(**args))


def download_all():
    for channel in config.sections():
        download(channel)
