import os
import logging
import re
import subprocess
import sys
import tempfile
import yaml

from invoke import task

from . import utils

@task()
def install_jekyll_site(ctx, path, dest):
    orig_path = os.getcwd()
    os.chdir(path)

    buildcmd = "make build"
    logging.debug("BUILD: {}".format(buildcmd))
    ctx.run(buildcmd)

    if not dest.endswith('/'):
        dest = "{}/".format(dest)

    clonecmd = "rsync -avhP --delete-delay {} {}".format("_site/", dest)

    logging.debug("COMMAND: {}".format(clonecmd))
    ctx.run(clonecmd)
    os.chdir(orig_path)
