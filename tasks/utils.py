import inspect
import logging
import subprocess
import os
import sys
import types

from invoke import task
from pprint import pprint

@task
def check_ssh_agent(ctx):
    try:
        logging.debug("Checking SSH agent has key(s) loaded")
        output = subprocess.check_output(["ssh-add", "-l"], universal_newlines=True)
    except subprocess.CalledProcessError as e:
        logging.error("Something went wrong with checking your ssh-agent list, try running ssh-add")
        sys.exit(1)

    if len(output.split("\n")) < 1:
        logging.warning("You have no keys available to forward, you may experience issues pulling content from Gitlab, please add and retry...")
        sys.exit(1)

@task
def text_context(ctx):
    logging.debug("Outputting invokes context")
    pprint(ctx)

@task
def ch_rundir(ctx):
    logging.debug("Changing directory")
    old_pwd = os.getcwd()
    os.chdir("ansible")
