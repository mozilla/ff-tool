import os
import shutil
from fabric.api import local


cmd_hdiutil = local("which hdiutil", capture=True)


def replace_ext(filename, ext):
    """
    Takes a filename, and changes it's extension.
    """
    basename = os.path.splitext(filename)[0]
    args = {"basename": basename, "ext": ext}
    return "{basename}.{ext}".format(**args)


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


def extract_dmg(dmg_path, app_src_filename, channel):
    """
    Mount the *.dmg image, copy the *.app file, then unmount the *.dmg image.
    """
    dmg_dirname = os.path.dirname(dmg_path)
    dmg_filename = os.path.basename(dmg_path)
    app_dest_filename = replace_ext(dmg_filename, "app")
    tmp_dirname = os.path.join(dmg_dirname, "_dmg_temp")
    app_src_path = os.path.join(tmp_dirname, app_src_filename)
    app_dest_path = os.path.join(dmg_dirname, app_dest_filename)

    attach(dmg_path, mountpoint=tmp_dirname)
    move_app(app_src_path, app_dest_path)
    detach(mountpoint=tmp_dirname)
    ver = get_firefox_version(app_dest_path)
    print("Installed {0} ({1})".format(ver, channel))


def get_firefox_version(app):
    bin = os.path.join(app, "Contents", "MacOS", "firefox")
    if not os.path.exists(bin):
        print("{0} not found. Aborting.".format(bin))
        return

    cmd = "{0} --version".format(bin)
    output = local(cmd, capture=True)
    for line in output.splitlines():
        return line
