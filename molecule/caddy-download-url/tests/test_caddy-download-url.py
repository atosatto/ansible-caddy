
def test_caddy_binary(host):

    caddy = host.file('/usr/local/bin/caddy')
    assert caddy.exists
    assert caddy.is_symlink
    assert caddy.linked_to == '/opt/caddy/caddy'


def test_caddy_plugins(host):

    cmd = host.run('/usr/local/bin/caddy --plugins')

    assert 'http.prometheus' in (cmd.stdout + cmd.stderr)
