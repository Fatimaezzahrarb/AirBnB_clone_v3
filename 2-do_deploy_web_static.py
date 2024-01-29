#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
import os
from fabric.api import put, env, run

env.hosts = ["54.160.113.165", "34.227.93.131"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """deploy package"""
    if not archive_path or not os.path.isfile(archive_path):
        print("Invalid archive path or file does not exist.")
        return False

    archive_name = os.path.basename(archive_path)
    release_name = archive_name.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(release_name))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
        archive_name, release_name))
    run("rm /tmp/{}".format(archive_name))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
        release_name))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/current/web_static")

    print("Deployment completed successfully.")
    return True
