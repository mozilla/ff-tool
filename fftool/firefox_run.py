import os

from firefox_env_handler import IniHandler

try:
    import configparser  # Python 3
except:
    import ConfigParser as configparser  # Python 2

from fabric.api import local  # It looks like Fabric may only support Python 2.

PATH_PROJECT = os.path.abspath('.')
PATH_TEMP = os.path.join(PATH_PROJECT, '_temp', 'profiles')
FILE_PREFS = 'prefs.ini'

config = configparser.ConfigParser()

env = IniHandler()
env.load_os_config('configs')


def launch_firefox(profile_path, channel):
    """
    this will be an all-encompassing function that may make use of all the
    others (with the exception of uninstall
    """

    # we need to invoke each of these here
    print("1. download firefox! (if not already)")
    print("2. install firefox! (if not already)")
    print("3. create profile! (unless we specify an existing)")
    print("4. Launch firefox!")

    FIREFOX_APP_BIN = env.get(channel, 'PATH_FIREFOX_BIN_ENV')
    PROFILE_PATH = os.path.join(PATH_TEMP, profile_path)

    cmd = "{0} -profile {1}".format(FIREFOX_APP_BIN, PROFILE_PATH)
    local(cmd)
