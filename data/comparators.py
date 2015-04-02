__author__ = 'Kenzie Togami'
import re
from datalib import compare
from semantic_version import Version
LESS = -1
EQUAL = 0
GREATER = 1


def tconcmp():
    from collections import defaultdict
    # tcon: <numeric><bug release>?<other stuff we don't care about>
    tcon = re.compile('(\d\.\d\.\d)(?:([a-z])|(?:RC(\d)))?')
    # ordering:
    # release candidates before regular
    # bugfixes after regular

    def cmp(a, b):
        data = defaultdict(dict)
        da = data['a']
        db = data['b']
        da['ref'] = a
        db['ref'] = b

        def setto(targetkey, function, *funckeys):
            avals = [da[k] for k in funckeys]
            bvals = [db[k] for k in funckeys]
            da[targetkey] = function(*avals)
            db[targetkey] = function(*bvals)

        setto('match', lambda ref: tcon.match(ref.version), 'ref')
        if not (da['match'] or db['match']):
            raise ValueError('{} or {} not comparable'.format(a, b))
        setto('length', lambda match: match.groups(), 'match')
        setto('version', lambda match: match.group(1), 'match')
        setto('bugfix', lambda match: match.group(2) or '', 'match')
        setto('rc#', lambda match: int(match.group(3) or 2**31), 'match')
        setto('semver', Version.coerce, 'version')
        return (compare(da['semver'], db['semver'])
                or compare(da['rc#'], db['rc#'])
                or compare(da['bugfix'], db['bugfix']))

    return cmp