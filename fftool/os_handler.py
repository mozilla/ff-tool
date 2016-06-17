#!/usr/bin/env python

import platform
import re

from outlawg import Outlawg

Log = Outlawg()


class OSHandler(object):

    @staticmethod
    def get_os():
        system = platform.system().lower()
        system = re.split('[-_]', system, maxsplit=1).pop(0)

        if system == "cygwin":
            return "windows"

        if system == "darwin":
            return "mac"

        return system

    @classmethod
    def is_linux(cls):
        return cls.get_os() == "linux"

    @classmethod
    def is_mac(cls):
        return cls.get_os() == "mac"

    @classmethod
    def is_other(cls):
        """Unrecognized OS"""
        return not (cls.is_linux() or cls.is_mac() or cls.is_windows())

    @classmethod
    def is_windows(cls):
        return cls.get_os() == "windows"
