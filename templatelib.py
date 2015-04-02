__author__ = 'Kenzie Togami'
from abc import ABC, abstractmethod
from semantic_version import Version
from bs4 import BeautifulSoup
from datalib import compare

Soup = lambda text: BeautifulSoup(text, 'lxml')


def urljoin(base, *args):
    from urllib.parse import urljoin as _urljoin

    inbetween = base
    for arg in args:
        inbetween = _urljoin(inbetween, arg)
    return inbetween


class Template(ABC):
    @abstractmethod
    def parse_site(self, mod, req, max_ver):
        return None, None

    def collect_changelogs(self, old_mod, new_mod):
        return None

    @abstractmethod
    def will_process(self, site):
        return False


class EasyTemplate(Template, ABC):
    @abstractmethod
    def will_process(self, site):
        pass

    @abstractmethod
    def get_mod_list(self, mod, req):
        pass

    @abstractmethod
    def get_version(self, mod, item):
        pass

    @abstractmethod
    def get_url(self, mod, item, ver):
        pass

    def compare_version(self, mod, a, b):
        return compare(Version.coerce(a), Version.coerce(b))

    def listindexprocessor(self):
        return lambda l: l

    def parse_site(self, mod, req, max_ver):
        mods = self.get_mod_list(mod, req)
        cachever = None
        cacheurl = None
        for i in self.listindexprocessor()(range(len(mods))):
            proposed_mod = mods[i]
            ver = self.get_version(mod, proposed_mod)
            url = self.get_url(mod, proposed_mod, ver)
            if max_ver:
                res = self.compare_version(mod, ver, max_ver)
                if res > 0:  # version bigger than max
                    print("{} has an upgrade to {}, but is limited to {}".format(mod.name, ver, max_ver))
                    continue
                elif res == 0:  # perfect!
                    pass
                else:  # store just in case
                    cachever = ver
                    cacheurl = url
                    continue
            return ver, url
        return cachever, cacheurl
