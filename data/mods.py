__author__ = 'Kenzie Togami'
from modlib import Mod
from data.comparators import *


MODS = [Mod(name='Buildcraft', site='http://www.mod-buildcraft.com/releases/BuildCraft/',
            do_not_pass='6.4.6'),
        Mod(name='IndustrialCraft2',
            site='http://jenkins.ic2.player.to/job/IC2_experimental/lastSuccessfulBuild/artifact/build/libs/'),
        Mod(name='Thaumcraft', site='http://minecraft.curseforge.com/mc-mods/223628-thaumcraft/files'),
        Mod(name="Tinker's Construct",
            site='http://minecraft.curseforge.com/mc-mods/74072-tinkers-construct/files',
            do_not_pass='1.7.1d').with_version(None, tconcmp(), True)]

__all__ = ['MODS']
