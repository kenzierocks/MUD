__author__ = 'Kenzie Togami'
from abc import ABC, abstractmethod
Soup = __import__('bs4').BeautifulSoup


def urljoin(base, *args):
    from urllib.parse import urljoin as _urljoin
    inbetween = base
    for arg in args:
        inbetween = _urljoin(inbetween, arg)
    return inbetween


class Template(ABC):
    @abstractmethod
    def parse_site(self, mod, req):
        return None, None

    def collect_changelogs(self, mod):
        return None

    @abstractmethod
    def will_process(self, site):
        return False

