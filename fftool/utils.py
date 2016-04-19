FAKE_SPACE = '~'
SPACE = ' '


class WinUtils(object):

    @staticmethod
    def filepath_real(filepath_fake_space):
        return filepath_fake_space.replace(FAKE_SPACE, SPACE)
