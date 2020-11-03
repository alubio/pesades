# pesades.py tests

import sys
sys.path.append("./src")
from pesades import __version__

def test_version():
    import re
    versionpattern = re.compile(r'^\d+(\.\d+){2,3}$') # Major.Minor.Patch
    assert versionpattern.match(__version__)
