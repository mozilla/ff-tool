import os
from subprocess import Popen, PIPE


__version__ = '0.1.1'


CHANNELS = ['release',
            'beta',
            'aurora',
            'nightly']

DEFAULT_CHANNEL = 'nightly'

HERE = os.path.dirname(os.path.realpath(__file__))
DIR_TEMP = '_temp'
DIR_TEMP_BROWSERS = os.path.join(DIR_TEMP, 'browsers')
DIR_CONFIGS = '{0}/configs'.format(HERE)
DIR_TEMP_PROFILES = os.path.join(DIR_TEMP, 'profiles')
PATH_PREFS_ROOT = os.environ.get('PATH_PREFS_ROOT')
FILE_PREFS = 'prefs.ini'
PLUS = '+'


def local(cmd, logging=False):
    proc = Popen(cmd, stdout=PIPE, shell=True)
    if logging:
        # return proc.stdout.read().strip()
        for line in iter(proc.stdout.readline, b''):
            print(line.strip())
    proc.stdout.close()
