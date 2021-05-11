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
Tests for operators_ds.py module.
"""

import sys
sys.path.append("./src")
from operators_ds import *

def test_store_operator():
    """Test store_operator"""
    assert store_operator("testnotuse", "testnotuse", "testnotuse", "admin", "+34919191919", "testnotuse@example.com", "testnotuse") == "OK"
    assert store_operator("testnotuse", "testnotuse", "testnotuse", "admin", "+34919191919", "testnotuse@example.com", "testnotuse") == "Username already exists. Please select another one."
