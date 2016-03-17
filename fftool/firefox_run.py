import os

from subprocess import Popen, PIPE
from fftool import (
    DIR_TEMP_PROFILES as BASE_PROFILE_DIR,
    OS_CONFIG as env
)


def launch_firefox(profile_path, channel):
    """
    This function will rely on the other functions (download, install, profile)
    having successfully done their business.
    """

    FIREFOX_APP_BIN = env.get(channel, 'PATH_FIREFOX_BIN_ENV')
    PROFILE_PATH = os.path.join(BASE_PROFILE_DIR, profile_path)

    print("Launching Firefox {0} with profile: {1}".format(
        channel,
        profile_path)
    )
    cmd = '"{0}" -profile "{1}"'.format(FIREFOX_APP_BIN, PROFILE_PATH)
    Popen(cmd, stdout=PIPE, shell=True)
