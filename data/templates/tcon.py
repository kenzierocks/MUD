__author__ = 'Kenzie Togami'
from templatelib import Template, Soup, urljoin
from data.templates.templatebase.curseforge import CurseForgeBase


class TinkersConstruct(CurseForgeBase):
    def __init__(self):
        import re
        super().__init__(74072, re.compile(r'TConstruct-1\.7\.10-(.+?)\.jar'))


instance = TinkersConstruct()
