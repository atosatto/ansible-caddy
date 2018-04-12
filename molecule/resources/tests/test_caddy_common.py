import os
import testinfra.utils.ansible_runner


def test_caddy_config(host):

    f = host.file('/etc/caddy.conf')
    assert f.exists
    assert f.is_file
    assert f.user == 'www-data'
    assert f.group == 'www-data'
    assert oct(f.mode) == '0440'

    d = host.file('/etc/caddy.conf.d/')
    assert d.exists
    assert d.is_directory
    assert d.user == 'www-data'
    assert d.group == 'www-data'
    assert oct(d.mode) == '0555'

    host.run("/usr/local/bin/caddy -conf /etc/caddy.conf -validate").rc == 0


def test_caddy_ssl_folder(host):

    d = host.file('/etc/ssl/caddy/')
    assert d.exists
    assert d.is_directory
    assert d.user == 'www-data'
    assert d.group == 'www-data'
    assert oct(d.mode) == '0770'


def test_caddy_service(host):

    s = host.service('caddy')
    assert s.is_running
    assert s.is_enabled


def test_caddy_webserver(host):

    host.socket("tcp://127.0.0.1:8080").is_listening
