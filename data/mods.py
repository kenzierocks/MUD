__author__ = 'Kenzie Togami'
from modlib import Mod


MODS = sorted([Mod(name='Buildcraft', site='http://www.mod-buildcraft.com/releases/BuildCraft/'),
               Mod(name='IndustrialCraft2',
                   site='http://jenkins.ic2.player.to/job/IC2_experimental/lastSuccessfulBuild/artifact/build/libs/'),
              ], key=lambda mod: mod.name)

__all__ = ['MODS']
