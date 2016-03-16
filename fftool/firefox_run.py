import os

from firefox_env_handler import IniHandler
from fabric.api import local

PATH_PROJECT = os.path.abspath('.')
PATH_TEMP = os.path.join(PATH_PROJECT, '_temp', 'profiles')

env = IniHandler()
env.load_os_config('configs')


def launch_firefox(profile_path, channel):
    """
    This function will rely on the other functions (download, install, profile)
    having successfully done their business.
    """

    FIREFOX_APP_BIN = env.get(channel, 'PATH_FIREFOX_BIN_ENV')
    PROFILE_PATH = os.path.join(PATH_TEMP, profile_path)

    cmd = '{0} -profile "{1}"'.format(FIREFOX_APP_BIN, PROFILE_PATH)
    local(cmd, capture=True)
