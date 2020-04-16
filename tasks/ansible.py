import os
import logging
import re
import subprocess
import sys
import yaml

from invoke import task
from pprint import pprint
from glob import glob
from yaml import Dumper

#import utils
from . import utils

@task(default=True, pre=[
    utils.check_ssh_agent,
    utils.ch_rundir,
])
def run_playbook(ctx, playbook,
    environment = None,
    tags = None,
    user = None,
    hosts = None,
    prompt = False,
    dry = False):
    """Run a single playbook"""

    if not re.match(r'\.yml$', playbook):
        playbook = "{0}.yml".format(playbook)

    if not environment and "environment" in ctx.vars:
        environment = ctx.vars.environment
        logging.debug("Set to default environment: {}".format(environment))

    additional_arguments = ""

    if not user and "user" in ctx.vars:
        user = ctx.vars.user
        logging.debug("Set to default user: {}".format(user))
    else:
        additional_arguments += "-u {} ".format(user)

    if hosts:
        additional_arguments += "-l '{}' ".format(hosts)

    if prompt:
        additional_arguments += "-K "

    # TODO: There's a big gap in the parser for list type in invoke (issue #132)
    if tags:
        tag_list = tags.split(",")
        tag_str = " -t \"" + "\" -t \"".join(tag_list) + "\""
        additional_arguments += tag_str

    command = os.path.expandvars("ansible-playbook -v -b \
-e env={0}  \
{2} \
--vault-id $HOME/.vault_{0}.password \
-i inventory/{0} \
playbooks/{1}".format(
        environment, playbook, additional_arguments
    ))
    print(os.getcwd())

    logging.info("COMMAND: {0}".format(command))
    if not dry:
        ctx.run(command)

@task(pre=[
    utils.ch_rundir,
])
def server_facts(ctx, hostname, environment=None, user=None):
    if not environment:
        environment = ctx.vars.environment
        logging.debug("Set to default environment: {}".format(environment))

    if not user:
        user = ctx.vars.user
        logging.debug("Set to default user: {}".format(user))

    cmd = "ansible -m setup -u {} -i inventory/{} {}".format(user, environment, hostname)
    logging.debug("COMMAND: {}".format(cmd))
    ctx.run(cmd)

@task(pre=[
    # TODO: Better way to this within the invoke Collection?
    utils.ch_rundir
])
def install_requirements(ctx):
    cmd = "ansible-galaxy role install -r roles/requirements.yml"
    logging.debug("COMMAND: {}".format(cmd))
    ctx.run(cmd)


@task(pre=[
    # TODO: Better way to this within the invoke Collection?
    utils.ch_rundir
])
def gen_ssh_config(ctx):
    #ansible -i inventory/staging --list-hosts libvirt_host | grep -v 'hosts' | awk '{ print $1 }'
    # ssh root@staging-host 'virsh list --name' | grep -v '^$'
    # Host staging-proxy
    #   User root
    #   Hostname proxy
    #   ProxyJump staging-host
    # TODO: Key injection to kickstarts!
    pass
