"""
NOTE: THIS IS AN OSX SPECIFIC FILE, SPECIFICALLY FOR MOUNTING DMG FILES.
"""


import os
import shutil
from fabric.api import local

cmd_hdiutil = local("which hdiutil", capture=True)


def attach(dmg_path, mountpoint):
    args = {
        "hdiutil": cmd_hdiutil,
        "dmg_path": dmg_path,
        "mountpoint": mountpoint
    }
    cmd = "{hdiutil} attach {dmg_path} -mountpoint {mountpoint}".format(**args)
    local(cmd, capture=True)


def detach(mountpoint):
    args = {
        "hdiutil": cmd_hdiutil,
        "mountpoint": mountpoint
    }
    cmd = "{hdiutil} detach {mountpoint}".format(**args)
    local(cmd, capture=True)


def move_app(src, dest):
    if os.path.exists(dest):
        print("Deleting existing {0} file".format(dest))
        shutil.rmtree(dest)

    print("Moving {0} to {1}".format(src, dest))
    shutil.copytree(src, dest)


def extract_dmg(dmg_path, app_src_filename, app_dest_filename, channel):
    """
    Mount the *.dmg image, copy the *.app file, then unmount the *.dmg image.
    """
    dmg_dirname = os.path.dirname(dmg_path)
    tmp_dirname = os.path.join(dmg_dirname, "_dmg_temp")
    app_src_path = os.path.join(tmp_dirname, app_src_filename)
    app_dest_path = os.path.join(dmg_dirname, app_dest_filename)

    attach(dmg_path, mountpoint=tmp_dirname)
    move_app(app_src_path, app_dest_path)
    detach(mountpoint=tmp_dirname)
