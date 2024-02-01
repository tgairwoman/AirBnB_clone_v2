#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder."""
from fabric.api import local, env, run, put
from datetime import datetime
import os


env.hosts = ['ubuntu@54.198.80.67', 'ubuntu@100.26.152.235']

def do_pack():
    """pack a web_static folder to .tgz"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local('tar -czvf {} web_static'.format(path))
        return path
    except Exception:
        return None

def do_deploy(archive_path):
    """deploys web_static to web servers"""
    if os.path.exists(archive_path):
        _name_w_extension = archive_path.split('/')[-1]
        _name = archive_path.split('/')[-1].split('.')[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(_name_w_extension, _name))
        run("rm {}".format(_name_w_extension))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(_name, _name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static_current".format(_name))
        print("New version deployed!")
