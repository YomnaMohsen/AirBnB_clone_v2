#!/usr/bin/python3
"""creates and distributes an archive to your web servers,
using the function deploy based on do_deploy and do_pack"""


from fabric.api import local, env, run, put, task
import os

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """full deploy"""
    archive_path = ""
    try:
        files = os.listdir("versions")
        if len(files) == 1:
            archive_path = "versions/" + files[0]
    except Exception:
        archive_path = do_pack()
    return do_deploy(archive_path)
