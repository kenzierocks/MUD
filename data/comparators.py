__author__ = 'Kenzie Togami'
import re


def tconcmp():
    # tcon: <numeric><bug release>?<other stuff we don't care about>
    tcon = re.compile('(.+?)([a-z]?)')
    def cmp(a, b):
        ma = tcon.match(a.version)
        mb = tcon.match(b.version)
        if not (ma or mb):
            raise ValueError('{} or {} not comparable'.format(a, b))
        versionbasea = ma.group(1)
        versionbaseb = mb.group(1)
        lena = len(ma.groups())
        lenb = len(mb.groups())
        if lena == 2 and lenb == 3:
            return -1  # a < b
        return a >= b
    return cmp