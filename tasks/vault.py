import getpass
import logging
import os
import sys

from invoke import task

@task
def write_pass(ctx, name):
    try:
        password = getpass.getpass("Please enter the vault password: ")
    except getpass.GetPassWarning:
        logging.exception("Something wrong whilst reading the password")
        sys.exit(1)

    password_file = os.path.expandvars("$HOME/.vault_{0}.password".format(name))
    good_to_go = True

    if os.path.exists(password_file):
        good_to_go = False
        response = input("Are you sure you want to overwrite (y/n)?")

        if response.strip().lower() != 'y':
            logging.warning("Abandoning as user did not confirm overwrite")
        else:
            good_to_go = True

    if good_to_go:
        try:
            with open(password_file, "w") as fh:
                fh.write(password)
            os.chmod(password_file, 0o600)
        except Exception:
            logging.exception("Something went wrong, deleting file if required")
            if os.path.exists(password_file):
                os.unlink(password_file)
        else:
            logging.info("Vault password written...")
