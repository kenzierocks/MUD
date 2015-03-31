__author__ = 'Kenzie Togami'
from semantic_version import Version
from datalib import Comparable


class Mod:
    def __init__(self, name, site, template=None, dependencies=[], do_not_pass=None):
        self.name = name
        self.site = site
        self.template = template
        self.dependencies = dependencies
        self.is_dependency = False
        for dep in dependencies:
            dep.is_dependency = True
        self.max_version = do_not_pass

    def with_version(self, version, compare=None, silent_on_fail=False):
        if isinstance(self, ExtendedMod):
            extmod = self
            extmod.version = version
            extmod.comparator = compare or extmod.comparator
            return self
        return ExtendedMod(self, version, compare, silent_on_fail)

    def get_dep_string(self):
        return "dep" if self.is_dependency else "mod"

    def __common_str(self, apply):
        return "Mod(name={}, site={}, template={}, dependencies={}, do_not_pass={})".format(
            apply(self.name), apply(self.site), apply(self.template), apply(self.dependencies),
            apply(self.max_version))

    def __repr__(self):
        return self.__common_str(repr)

    def __str__(self):
        return self.__common_str(str)


class ExtendedMod(Mod, Comparable):
    @classmethod
    def __default_cmp(cls, a, b):
        if isinstance(b, ExtendedMod):
            return a.sver.__cmp__(b.sver)
        raise NotImplemented()

    def __init__(self, base, version, compare, silent):
        super().__init__(base.name, base.site, base.template, base.dependencies, base.max_version)
        self.version = version
        self.comparator = compare or (lambda s, o: ExtendedMod.__default_cmp(s, o))
        try:
            self.sver = Version.coerce(version)
        except:
            if not silent:
                import traceback
                traceback.print_exc()
                print(version)

    def get_versioned_file_name(self):
        s = "{} {} v{}.jar".format(self.name, self.get_dep_string(), self.version)
        s = "".join(i if not (i in "\/:*?<>|) ") else '_' for i in s)
        return s

    def __cmp__(self, other):
        return self.comparator(self, other)

    def __hash__(self):
        return self.sver.__hash__()

    def __repr__(self):
        return "{}.with_version({})".format(super().__repr__(), repr(self.version))

    def __str__(self):
        return "{} v{}".format(super().__str__(), self.version)
