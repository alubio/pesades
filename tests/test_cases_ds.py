# -*- coding: utf-8 -*-
"""
Tests for cases_ds.py module.
"""

import sys
sys.path.append("./src")
from cases_ds import *

def test_store_case():
    """Test store_case"""
    assert store_case("testnotuse", "testnotuse", "testnotuse", "+34919191919", "testnotuse@example.com") == "Case name really exist. Please select another one."
