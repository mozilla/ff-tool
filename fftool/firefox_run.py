import os
import shutil

try:
    import configparser  # Python 3
except:
    import ConfigParser as configparser  # Python 2

from fabric.api import local  # It looks like Fabric may only support Python 2.

PATH_PROJECT = os.path.abspath('.')
PATH_TEMP = os.path.join(PATH_PROJECT, '_temp', 'profiles')
FILE_PREFS = 'prefs.ini'

config = configparser.ConfigParser()

"""this will be an all-encompassing function that may make use of all the 
others (with the exception of uninstall"""
def launch_firefox(some_args_here):

    # we need to invoke each of these here 
    print("1. download firefox! (if not already)")
    print("2. install firefox! (if not already)")
    print("3. create profile! (unless we specify an existing)")
    print("4. Launch firefox!")
