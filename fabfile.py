#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static folder."""
from fabric.api import local
from datetime import datetime


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
