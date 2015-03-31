__author__ = 'Kenzie Togami'
from templatelib import Template, Soup, urljoin


class IC2(Template):
    import re
    regex = re.compile('^industrialcraft-(.+?)-experimental.jar$')

    @classmethod
    def parse_version(cls, filename):
        return cls.regex.match(filename).group(1)

    def parse_site(self, mod, req):
        soup = Soup(req.text)
        table = soup('table', class_='fileList')[0]
        trow = table('tr')[0]
        td = trow('td')[1]
        a = td('a')[0]
        version = IC2.parse_version(a.string)
        link = a['href']
        return version, urljoin(mod.site, link)

    def will_process(self, site):
        return site.startswith('http://jenkins.ic2.player.to/')


instance = IC2()
