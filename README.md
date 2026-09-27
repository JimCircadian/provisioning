# provisioning

## Overview

Ansible is executed via a collection of tasks implemented via `invoke`.

## Ansible

This repository is effectively the root of an ansible run directory, with invoke as a helper utility. Therefore, once you clone it and set up inventory and your variables to control the playbooks, you can get cracking with provisioning. This is much akin to any ansible setup, but this has some additional structure and helpfulness thrown in. 

### Structure

### Concept

### Basic Commands

Don't forget to `invoke ansible.install-requirements`

Running: `invoke ansible -e development server`

## TODO:

* (Samba)[https://github.com/vladgh/ansible-collection-vladgh-samba]
