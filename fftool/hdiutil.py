import os
import shutil
from fabric.api import local


cmd_hdiutil = None

output = local("which hdiutil", capture=True)
for line in output.splitlines():
    cmd_hdiutil = line


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
    """
    Loop over all the files in the `src` file's directory looking for any *.app
    file and copy it into the `dest` directory.
    """
    tmp_dir = os.path.dirname(src)
    # Loop over each file in the `temp_dir` looking for any *.app files.
    for file in os.listdir(tmp_dir):
        if file.endswith(".app"):
            # Once we match our *.app file, delete any existing file in the
            # `dest` folder and copy the new *.app over.
            src_path = os.path.join(tmp_dir, file)

            if os.path.exists(dest):
                print("Deleting existing {0} file".format(dest))
                shutil.rmtree(dest)

            print("Moving {0} to {1}".format(src_path, dest))
            shutil.copytree(src_path, dest)


def extract_dmg(file):
    """
    Mount the *.dmg, copy the *.app file, and unmount the *.dmg file.
    """
    dmg_dirname = os.path.dirname(file)
    dmg_filename = os.path.basename(file)
    app_filename = replace_ext(dmg_filename, "app")
    tmp_dir = os.path.join(dmg_dirname, "_dmg_temp")
    app_src_path = os.path.join(tmp_dir, app_filename)
    app_dest_path = os.path.join(dmg_dirname, app_filename)

    attach(file, mountpoint=tmp_dir)
    move_app(app_src_path, app_dest_path)
    detach(mountpoint=tmp_dir)
    ver = get_firefox_version(app_dest_path)
    print("Installed {0}".format(ver))


def get_firefox_version(app):
    bin = os.path.join(app, "Contents", "MacOS", "firefox")
    if not os.path.exists(bin):
        print("{0} not found. Aborting.".format(bin))
        return

    cmd = "{0} --version".format(bin)
    output = local(cmd, capture=True)
    for line in output.splitlines():
        return line


extract_dmg("_temp/browsers/FirefoxRelease.dmg")
extract_dmg("_temp/browsers/FirefoxBeta.dmg")
extract_dmg("_temp/browsers/FirefoxDevEdition.dmg")
extract_dmg("_temp/browsers/FirefoxNightly.dmg")
