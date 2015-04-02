__author__ = 'Kenzie Togami'
from templatelib import EasyTemplate, Soup, urljoin


class IC2(EasyTemplate):
    import re

    regex = re.compile('^industrialcraft-(.+?)-experimental.jar$')

    @classmethod
    def parse_version(cls, filename):
        return cls.regex.match(filename).group(1)

    @classmethod
    def __find_all_version_links(cls, tag):
        return tag.name == 'tr' and len(tag('td')) > 1

    def get_url(self, mod, item, ver):
        return urljoin(mod.site, item['href'])

    def get_mod_list(self, mod, req):
        # first, get the file list
        l = Soup(req.text)('table', class_='fileList')[0](IC2.__find_all_version_links)
        # next, map through the tr and a elements
        l = [trow('td')[1]('a')[0] for trow in l]
        return l

    def get_version(self, mod, item):
        return IC2.parse_version(item.string)

    def will_process(self, site):
        return site.startswith('http://jenkins.ic2.player.to/')


instance = IC2()
