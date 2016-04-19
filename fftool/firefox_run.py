from fftool import (
    OS_CONFIG as env,
    local
)


def launch_firefox(profile_path, channel):
    """
    This function will rely on the other functions (download, install, profile)
    having successfully done their business.
    """

    FIREFOX_APP_BIN = env.get(channel, 'PATH_FIREFOX_BIN_ENV')

    print("Launching Firefox {0} with profile: {1}".format(
        channel,
        profile_path)
    )

    #cmd = '"{0}" -profile "{1}"'.format(FIREFOX_APP_BIN, profile_path)
    cmd = '{0} -profile {1}'.format(FIREFOX_APP_BIN, profile_path)
    local(cmd)
