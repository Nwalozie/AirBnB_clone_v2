#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    timestamp = time.strftime("%Y%m%d%H%M%S")
    output = "versions/web_static_{}.tgz".format(timestamp)
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output
