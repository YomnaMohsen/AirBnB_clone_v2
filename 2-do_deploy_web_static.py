#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""


from fabric.api import put, run, env
import os.path


env.hosts = ['100.25.145.224', '18.209.225.166']


def do_deploy(archive_path):
    """deploy files on server"""
    if os.path.isdir(archive_path):
        return False
    file_ext = archive_path.split('/')[-1]
    file_name = file_ext.split('.')[0]
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(file_name))
        run('tar -zxf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_ext, file_name))
        run('rm -r /tmp/{}'.format(file_ext))
        run('mv data/web_static/releases/{}/web_static/*'
            '/data/web_static/releases/{}/'.format(file_name, file_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.
            format(file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(file_name))
        return True
    except Exception:
        return False
