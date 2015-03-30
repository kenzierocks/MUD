__author__ = 'Kenzie Togami'
import data.mods as modcfg
import fetch
import subprocess

for mod in modcfg.MODS:
    fetch.fetch_site_and_process(mod)

subprocess.check_call("gradle", shell=True)
