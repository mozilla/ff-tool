import os
from subprocess import Popen, PIPE, STDOUT
from outlawg import Outlawg


__version__ = '0.1.1'


CHANNELS = ['release',
            'beta',
            'nightly']

DEFAULT_CHANNEL = 'nightly'

HERE = os.path.dirname(os.path.realpath(__file__))
DIR_TEMP = '.cache'
DIR_TEMP_BROWSERS = os.path.join(DIR_TEMP, 'browsers')
DIR_CONFIGS = '{0}/configs'.format(HERE)
DIR_TEMP_PROFILES = os.path.join(DIR_TEMP, 'profiles')
PATH_PREFS_ROOT = os.environ.get('PATH_PREFS_ROOT')
FILE_PREFS = 'prefs.ini'

Log = Outlawg()


def local(cmd, logging=False):
    proc = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    if logging:
        Log.header("FIREFOX LOGS")
        for line in iter(proc.stdout.readline, b''):
            print(line.strip())
    else:
        result = proc.stdout.read().strip()
        proc.stdout.close()
    return result
