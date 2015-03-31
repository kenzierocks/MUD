__author__ = 'Kenzie Togami'
from templatelib import Template, Soup, urljoin
from data.templates.templatebase.curseforge import CurseForgeBase


class Thaumcraft(CurseForgeBase):
    def __init__(self):
        import re
        super().__init__(223628, re.compile(r'Thaumcraft-1\.7\.10-(.+?)\.jar'))


instance = Thaumcraft()
