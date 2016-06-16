import os
from outlawg import Outlawg
from fftool import (
    DIR_CONFIGS,
    local
)
from ini_handler import IniHandler

Log = Outlawg()
env = IniHandler()
env.load_os_config(DIR_CONFIGS)


def launch_firefox(profile_path, channel, logging, nspr_log_modules=''):
    """relies on the other functions (download, install, profile)
    having completed.
    """

    FIREFOX_APP_BIN = env.get(channel, 'PATH_FIREFOX_BIN_ENV')

    Log.header('LAUNCH FIREFOX')
    print("Launching Firefox {0} with profile: {1}".format(
        channel,
        profile_path)
    )

    cmd = '"{0}" -profile "{1}"'.format(FIREFOX_APP_BIN, profile_path)
    print('CMD: ' + cmd)

    # NSPR_LOG_MODULES
    if nspr_log_modules:
        Log.header('FIREFOX NSPR_LOG_MODULES LOGGING')
        os.environ['NSPR_LOG_MODULES'] = nspr_log_modules

    local(cmd, logging)
