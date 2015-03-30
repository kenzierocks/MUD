__author__ = 'Kenzie Togami'
import pickle
import os
from datalib import ReverseDict


# initial de-pickle
FILE = 'data/mods.pickle'
mod_dict = ReverseDict()


def load():
    if os.path.isfile(FILE):
        with open(FILE, "rb") as data:
            mod_dict.update(pickle.load(data))


def save():
    with open(FILE, "wb") as data:
        pickle.dump(mod_dict, data)


def find_version(mod):
    return mod_dict.invert().get(mod, None)


def put(extended_mod):
    version = extended_mod.version
    mod_dict[str(version)] = extended_mod

load()
