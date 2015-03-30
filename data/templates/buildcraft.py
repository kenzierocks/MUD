__author__ = 'Kenzie Togami'
from templatelib import Template, Soup, urljoin


class Buildcraft(Template):
    @classmethod
    def _find_all_version_links(cls, tag):
        return tag.name == 'a' and tag['href'] != '../'

    def parse_site(self, mod, req):
        soup = Soup(req.text)
        modslist = soup(Buildcraft._find_all_version_links)
        proposed_mod = modslist[-1]
        version = proposed_mod['href'][:-1]
        dl_link = urljoin(mod.site, proposed_mod['href'], 'buildcraft-' + version + '.jar')
        return version, dl_link

    def will_process(self, site):
        return site.startswith('http://www.mod-buildcraft.com/')

instance = Buildcraft()
