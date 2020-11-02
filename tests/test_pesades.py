# pesades.py tests

import sys
sys.path.append("./src")
from pesades import *

def test_version():
	assert "." in version()
