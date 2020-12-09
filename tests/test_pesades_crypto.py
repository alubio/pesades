# -*- coding: utf-8 -*-
#
# Copyright 2021 Iván Paniagua Barrilero
#
# This file is part of PESADES.
#
# PESADES is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PESADES is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PESADES.  If not, see <https://www.gnu.org/licenses/>.

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