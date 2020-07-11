import logging

from invoke import Collection

from . import ansible, deploy, utils, vault

logging.getLogger().setLevel(logging.INFO)
ns = Collection(ansible, deploy, vault)
