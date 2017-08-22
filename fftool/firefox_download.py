"""Module to download OS-specific versions of Firefox:
1. Nightly (nightly)
2. Beta (beta)
3. General Release (release)
"""

import os
import time
from requests.exceptions import ConnectionError
import ConfigParser as configparser  # Python 2 only!

from outlawg import Outlawg
from fftool import (
    DIR_TEMP_BROWSERS as BASE_DIR,
    DIR_CONFIGS,
)
from firefox_install import install, get_firefox_version
from ini_handler import IniHandler
from mozdownload import FactoryScraper

env = IniHandler()
env.load_os_config(DIR_CONFIGS)

CONFIG_CHANNELS = os.path.join(DIR_CONFIGS, 'channels.ini')
SCRIPT_START_TIME = time.time()

config = configparser.ConfigParser()
config.read(CONFIG_CHANNELS)
Log = Outlawg()


def modification_date(filename):
    try:
        mtime = os.path.getmtime(filename)
    except OSError as e:
        Log.header('ERROR!')
        print(e)
        exit()
    return mtime


def download(channel):

    Log.header('DOWNLOAD FIREFOX')

    ch_type = config.get(channel, 'type')
    ch_version = config.get(channel, 'version')
    ch_branch = config.get(channel, 'branch')
    # PLATFORM is uppercased here since the platform comes from the OS-specific
    # config files, whereas the other flags generically come from channels.ini.
    ch_platform = env.get(channel, 'PLATFORM')

    download_filename = env.get(channel, 'DOWNLOAD_FILENAME')
    download_path = os.path.join(BASE_DIR, download_filename)

    args = {"channel": channel, "download_path": download_path}
    print("Downloading {channel} to {download_path}".format(**args))

    try:
        scraper = FactoryScraper(
            ch_type,
            version=ch_version,
            branch=ch_branch,
            destination=download_path,
            platform=ch_platform
        )
        scraper.download()
    except ConnectionError:
        Log.header('WARNING!')
        print('HTTPS connection unavailable.\nLooking for cached browser...')

    is_recent_file = modification_date(download_path) > SCRIPT_START_TIME
    firefox_bin = env.get(channel, 'PATH_FIREFOX_BIN_ENV')

    # If the *.dmg file was downloaded recently, or we don't have the *.app
    # file installed, install current Firefox channel.

    if is_recent_file or not os.path.exists(firefox_bin):
        install(channel)

    else:
        firefox_version = get_firefox_version(channel)
        args = {"channel": channel, "version": firefox_version}
        msg = "You have the latest version of {channel} installed ({version})."
        Log.header('BROWSER VERSION')
        print(msg.format(**args))


def download_all():
    for channel in config.sections():
        download(channel)
