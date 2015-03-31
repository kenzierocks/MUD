__author__ = 'Kenzie Togami'
import data.mods as modcfg
import fetch
import subprocess
import os

for mod in sorted(modcfg.MODS, key=lambda cfg: cfg.name):
    fetch.fetch_site_and_process(mod)

print('TEMPORARY: not gradling')
__import__('sys').exit()
print('Launching gradle...')
env = dict(os.environ)
env['GRADLE_INCREMENTAL'] = 'false'
subprocess.check_call("gradle --daemon -i -x buildLauncher", env=env, shell=True)
