__author__ = 'Kenzie Togami'
from modlib import Mod


mod_buildcraft = Mod(name='Buildcraft', site='http://www.mod-buildcraft.com/releases/BuildCraft/')


MODS = [y for x, y in dict(locals()).items() if x.startswith('mod_')]
