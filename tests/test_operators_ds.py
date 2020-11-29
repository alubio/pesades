# -*- coding: utf-8 -*-
"""
Tests for operators_ds.py module.
"""

import sys
sys.path.append("./src")
from operators_ds import *

def test_store_operator():
    """Test store_operator"""
    assert store_operator("testnotuse", "testnotuse", "testnotuse", "+34919191919", "testnotuse@example.com", "testnotuse") == "Username really exist. Please select another one."

def test_check_password():
    """Test check_password"""
    #assert check_userpassword("testnotuse", "testnotuse")
    # TODO
    assert True
