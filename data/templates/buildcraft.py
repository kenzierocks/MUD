__author__ = 'Kenzie Togami'
from templatelib import EasyTemplate, Soup, urljoin
from semantic_version import Version


class Buildcraft(EasyTemplate):
    @classmethod
    def _find_all_version_links(cls, tag):
        return tag.name == 'a' and tag['href'] != '../'

    def get_url(self, mod, item, ver):
        return urljoin(mod.site, item['href'], 'buildcraft-' + ver + '.jar')

    def get_mod_list(self, mod, req):
        return Soup(req.text)(Buildcraft._find_all_version_links)

    def get_version(self, mod, item):
        return item['href'][:-1]

    def listindexprocessor(self):
        return reversed

    def will_process(self, site):
        return site.startswith('http://www.mod-buildcraft.com/')

instance = Buildcraft()
