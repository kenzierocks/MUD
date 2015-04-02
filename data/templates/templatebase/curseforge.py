__author__ = 'Kenzie Togami'
from templatelib import EasyTemplate, Soup, urljoin
from semantic_version import Version


class CurseForgeBase(EasyTemplate):
    def __init__(self, project_id, regex):
        """
        Creates the CurseForgeBase, using the regex to match versions.

        :param project_id: CF project ID
        :param regex: Version matcher regex, group(1) must be a valid version.
        """
        self.project_id = str(project_id)
        self.regex = regex

    def get_url(self, mod, item, ver):
        return urljoin(mod.site, item['href'])

    def compare_version(self, mod, a, b):
        if hasattr(mod, 'comparator'):
            return mod.comparator(mod.with_version(a), mod.with_version(b))
        else:
            return super().compare_version(mod, a, b)

    def get_mod_list(self, mod, req):
        return Soup(req.text)('a', class_='overflow-tip')

    def get_version(self, mod, item):
        match = self.regex.match(item.string)
        if not match:
            raise ValueError('Invalid regex provided by {}\nMatching {}'.format(type(self).__name__,
                                                                                repr(item.string)))
        return match.group(1)

    def will_process(self, site):
        httpcutoff = site.index('://')
        return (site[httpcutoff + 3:].startswith('minecraft.curseforge.com') and
                self.project_id in site and site.endswith('files'))
