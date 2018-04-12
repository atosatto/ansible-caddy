"""Prometheus Jinja2 filters"""
import re


CADDY_SYSTEM =  {
    'Linux': 'linux',
    'Darwin': 'darwin',
    'FreeBSD': 'freebsd',
    'OpenBSD': 'openbsd'
}

CADDY_ARCHITECTURE = {
    'x86_64': 'amd64',
    'i386': '386',
    'armv6l': 'armv6',
    'armv7l': 'armv7'
}


def caddy_release_build(hostvars, caddyrelease):

    architecture = hostvars['ansible_architecture']
    system = hostvars['ansible_system']

    return 'caddy_' + caddyrelease + '_' + CADDY_SYSTEM[system] + '_' + CADDY_ARCHITECTURE[architecture]


class FilterModule(object):


    def filters(self):
        return {
            'caddy_release_build': caddy_release_build
        }
