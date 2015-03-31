__author__ = 'Kenzie Togami'
import data.mods as modcfg
import fetch
import subprocess
import os

for mod in modcfg.MODS:
    fetch.fetch_site_and_process(mod)

print('Launching gradle...')
env = dict(os.environ)
env['GRADLE_INCREMENTAL'] = 'false'
subprocess.check_call("gradle --daemon -i -x buildLauncher", env=env, shell=True)
