#!/usr/bin/python3
"""creates and distributes an archive to your web servers, 
using the function deploy based on do_deploy and do_pack"""


from fabric.api import local, env, run, put
import os.path
from datetime import datetime

env.hosts = ['100.25.145.224', '18.209.225.166']
env.user = ['ubuntu', 'ubuntu']


def do_pack():
    """generates .tgz file"""
    try:
        local('mkdir -p versions')
        dt = datetime.utcnow()
        f_name = "web_static_{}{}{}{}{}{}.tgz".format(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        local("tar cvzf versions/{} web_static".format(f_name))
        return "versions/f_name"
    except Exception:
        return None
    
def do_deploy(archive_path):
    """deploy files on server"""
    if not os.path.isfile(archive_path):
        return False
    file_ext = archive_path.split('/')[-1]
    file_name = file_ext.split('.')[0]
    try:
        put(archive_path, '/tmp/{}'.format(file_ext))
        run('mkdir -p /data/web_static/releases/{}'.format(file_name))
        run('tar -zxf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_ext, file_name))
        run('rm -r /tmp/{}'.format(file_ext))
        run('mv /data/web_static/releases/{}/web_static/*  '
            '/data/web_static/releases/{}/'.format(file_name, file_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.
            format(file_name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(file_name))
        return True
    except Exception as e:
        return False
    
def deploy():
    """dist archives to web servers"""
    if (do_pack() is not None):
        return (do_deploy(do_pack()))
    else:
        return False    