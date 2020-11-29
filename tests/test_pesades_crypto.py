# -*- coding: utf-8 -*-
"""
Tests for pesades_crypto.py module.
"""

import sys
sys.path.append("./src")
from pesades_crypto import *

def test_is_weakpassword():
    """Test password strength"""
    assert is_weakpassword("PAssw0rd,chulade10") == False
    assert is_weakpassword("123456") == True
    assert is_weakpassword("password") == True
    assert is_weakpassword("pass#word") == True
    assert is_weakpassword("passwordde10") == True
    assert is_weakpassword("Pas,word10") == True

def test_is_passwordok():
    """Test password comparison"""
    assert is_passwordok("PAssw0rd,chulade10", get_hashedpassword("PAssw0rd,chulade10")) == True
    assert is_passwordok("Aversicuela", get_hashedpassword("PAssw0rd,chulade10")) == False