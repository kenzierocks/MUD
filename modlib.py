__author__ = 'Kenzie Togami'
from semantic_version import Version
from datalib import Comparable


class Mod:
    def __init__(self, name, site, template=None, dependencies=[]):
        self.name = name
        self.site = site
        self.template = template
        self.dependencies = dependencies
        self.is_dependency = False
        for dep in dependencies:
            dep.is_dependency = True

    def with_version(self, version):
        if isinstance(self, ExtendedMod):
            extmod = self
            extmod.version = version
            return self
        return ExtendedMod(self, version)

    def get_dep_string(self):
        return "dep" if self.is_dependency else "mod"

    def __common_str(self, apply):
        return "Mod(name={}, site={}, template={}, dependencies={})".format(
            apply(self.name), apply(self.site), apply(self.template), apply(self.dependencies))

    def __repr__(self):
        return self.__common_str(repr)

    def __str__(self):
        return self.__common_str(str)


class ExtendedMod(Mod, Comparable):
    def __init__(self, base, version):
        super().__init__(base.name, base.site, base.template, base.dependencies)
        self.version = version
        try:
            self.sver = Version.coerce(version)
        except:
            import traceback
            traceback.print_exc()
            pass

    def get_versioned_file_name(self):
        s = "{} {} v{}.jar".format(self.name, self.get_dep_string(), self.version)
        s = "".join(i if not (i in "\/:*?<>|) ") else '_' for i in s)
        return s

    def __cmp__(self, other):
        if isinstance(other, ExtendedMod):
            return self.sver.__cmp__(other.sver)
        return False

    def __hash__(self):
        return self.sver.__hash__()

    def __repr__(self):
        return "{}.with_version({})".format(super().__repr__(), repr(self.version))

    def __str__(self):
        return "{} v{}".format(super().__str__(), self.version)
