__author__ = 'Kenzie Togami'
import pickle
import os


# initial de-pickle
FILE = 'data/mods.pickle'
mod_dict = dict()


def load():
    if os.path.isfile(FILE):
        with open(FILE, "rb") as data:
            mod_dict.update(pickle.load(data))
            print(mod_dict)


def save():
    with open(FILE, "wb") as data:
        pickle.dump(mod_dict, data)


def find_version(mod):
    return mod_dict.get(mod, None)


def put(extended_mod):
    version = extended_mod.version
    mod_dict[extended_mod] = version

load()
