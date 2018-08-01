import os
import re
from github import Github

gh = Github(os.getenv('TRAVIS_GH_TOKEN', None))
caddy_last_release = re.sub('^v(.*)$', '\\1', gh.get_repo('mholt/caddy').get_latest_release().tag_name)
caddy_last_artifact = "caddy_v" + caddy_last_release + "_linux_amd64"


def test_caddy_binary(host):

    caddy = host.file('/usr/local/bin/caddy')
    assert caddy.exists
    assert caddy.is_symlink
    assert caddy.linked_to == '/opt/' + caddy_last_artifact + '/caddy'


def test_caddy_release(host):

    cmd = host.run('/usr/local/bin/caddy --version')

    assert 'Caddy ' + caddy_last_release in (cmd.stdout + cmd.stderr)
