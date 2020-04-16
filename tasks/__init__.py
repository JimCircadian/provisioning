import logging

from invoke import Collection

from . import ansible, utils, vault

logging.getLogger().setLevel(logging.INFO)
ns = Collection(ansible)
