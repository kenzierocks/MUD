__author__ = 'Kenzie Togami'
from modlib import Mod


mod_buildcraft = Mod(name='Buildcraft', site='http://www.mod-buildcraft.com/releases/BuildCraft/')
mod_ic2 = Mod(name='IndustrialCraft2',
              site='http://jenkins.ic2.player.to/job/IC2_experimental/lastSuccessfulBuild/artifact/build/libs/')


MODS = [y for x, y in dict(locals()).items() if x.startswith('mod_')]
