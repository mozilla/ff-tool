import os
from subprocess import Popen, PIPE
from firefox_env_handler import IniHandler

__version__ = '0.0.1'


CHANNELS = ['release',
            'beta',
            'aurora',
            'nightly',
            'ALL']

DEFAULT_CHANNEL = 'nightly'

DIR_TEMP = '_temp'
DIR_TEMP_BROWSERS = os.path.join(DIR_TEMP, 'browsers')
DIR_TEMP_PROFILES = os.path.join(DIR_TEMP, 'profiles')

OS_CONFIG = IniHandler()
OS_CONFIG.load_os_config('configs')

PATH_PREFS_ROOT = os.environ.get('PATH_PREFS_ROOT')


def local(cmd):
    output = Popen(cmd, stdout=PIPE, shell=True)
    return output.stdout.read().strip()
