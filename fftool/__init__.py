import os
from subprocess import Popen, PIPE
from firefox_env_handler import IniHandler
from outlawg import Outlawg


__version__ = '0.0.1'


CHANNELS = ['release',
            'beta',
            'aurora',
            'nightly',
            'ALL']

DEFAULT_CHANNEL = 'nightly'

DIR_TEMP = '_temp'
DIR_TEMP_BROWSERS = os.path.join(DIR_TEMP, 'browsers')

OS_CONFIG = IniHandler()
OS_CONFIG.load_os_config('configs')

if IniHandler.is_windows():
    DIR_TEMP_PROFILES = os.environ.get('PATH_FIREFOX_PROFILES') 
else:
    DIR_TEMP_PROFILES = os.path.join(DIR_TEMP, 'profiles')

PATH_PREFS_ROOT = os.environ.get('PATH_PREFS_ROOT')

Log = Outlawg()


def local(cmd):
    output = Popen(cmd, stdout=PIPE, shell=True)
    return output.stdout.read().strip()
