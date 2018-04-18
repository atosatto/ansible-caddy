Ansible Role: Caddy
===================

[![Build Status](https://travis-ci.org/atosatto/ansible-caddy.svg?branch=master)](https://travis-ci.org/atosatto/ansible-caddy)
[![Galaxy](https://img.shields.io/badge/galaxy-atosatto.caddy-blue.svg?style=flat-square)](https://galaxy.ansible.com/atosatto/caddy)

Install and configure Caddy.

Requirements
------------

An Ansible 2.2 or higher installation.<br />
This role makes use of the Ansible `json_filter` that requires `jmespath` to be installed on the Ansible machine.
See the `requirements.txt` file for further details on the specific version of `jmespath` required by the role.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

    caddy_release_tag: "latest"

The Caddy release to be installed.
By default, the latest release published at https://github.com/caddy/caddy/releases.

    caddy_user: "caddy"
    caddy_group: "caddy"

Caddy system user and group.

    caddy_install_path: "/opt"

Directory containing the downloaded Caddy release artifacts.

    caddy_bin_path: "/usr/local/bin"

Directory to which the Caddy biyy will be symlinked.

    caddy_config_file: "/etc/caddy.conf"

Path to the main Caddy configuration file.

    caddy_config_import_path: "/etc/caddy.conf.d"
    caddy_config_import_files: {}

Directory including Caddy's additional configuration files to be imported in the `caddy_config_file` file.

    caddy_ssl_certificates_path: "/etc/ssl/caddy"

The Caddy listen ip address and port.

    caddy_web_root: "/var/www"

Caddy HTTP server default Web folder.

    caddy_log_path: "/var/log/caddy"

Directory containing Caddy logs files

    caddy_additional_cli_args: ""

Additional command-line arguments to be added to the Caddy service unit.
For the complete refence of the available CLI arguments please refer to the output
of the `caddy --help` command.

Dependencies
------------

None.

Example Playbooks
-----------------

    $ cat playbook.yml
    - name: "Install and configure Caddy"
      hosts: all
      roles:
        - { role: atosatto.caddy }

Testing
-------

Tests are automated with [Molecule](http://molecule.readthedocs.org/en/latest/).

    $ pip install tox

To test all the scenarios run

    $ tox

To run a custom molecule command

    $ tox -e py27-ansible23 -- molecule test -s caddy-latest

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
