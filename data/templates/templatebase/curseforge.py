__author__ = 'Kenzie Togami'
from templatelib import Template, Soup, urljoin


class CurseForgeBase(Template):
    def __init__(self, project_id, regex):
        """
        Creates the CurseForgeBase, using the regex to match versions.

        :param project_id: CF project ID
        :param regex: Version matcher regex, group(1) must be a valid version.
        """
        self.project_id = str(project_id)
        self.regex = regex

    def parse_site(self, mod, req):
        soup = Soup(req.text)
        overflowtiplinks = soup('a', class_='overflow-tip')
        link = overflowtiplinks[0]
        match = self.regex.match(link.string)
        if not match:
            raise ValueError('Invalid regex provided by {}\nMatching {}'.format(self.__class__.__name__,
                                                                                repr(link.string)))
        return match.group(1), urljoin(mod.site, link['href'])

    def will_process(self, site):
        httpcutoff = site.index('://')
        return (site[httpcutoff + 3:].startswith('minecraft.curseforge.com') and
                self.project_id in site and site.endswith('files'))
