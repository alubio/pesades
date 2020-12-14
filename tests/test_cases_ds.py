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
Tests for cases_ds.py module.
"""

import sys
sys.path.append("./src")
from cases_ds import *

def test_process_case():
    """Test case creation, update and deletion"""
    assert store_case("testnotuse1", "idnotuse1", "testnotuse1", "testnotuse1", "+34919191919", "testnotuse1@example.com", False) == "OK"
    assert update_case("testnotuse1", "testnotuse2", "idnotuse2", "testnotuse2", "testnotuse2", "+34222222222", "testnotuse2@example.com", False) == "OK"
    assert update_case("testnotuse2", "testnotuse3", "idnotuse3", "testnotuse3", "testnotuse3", "+34233333333", "testnotuse3@example.com", False) == "OK"
    assert delete_case("testnotuse3") == "OK"
    assert delete_case("testnotuse2") == "Case does not exist"
    assert delete_case("testnotuse1") == "Case does not exist"
    assert store_case("testnotuse1", "idnotuse1", "testnotuse1", "testnotuse1", "+34919191919", "testnotuse1@example.com", False) == "OK"
    assert store_case("testnotuse1", "idnotuse1", "testnotuse1", "testnotuse1", "+34919191919", "testnotuse1@example.com", False) == "Case name already exists. Please select another one."
    assert store_case("testnotuse2", "idnotuse1", "testnotuse1", "testnotuse1", "+34919191919", "testnotuse1@example.com", False) == "Case ID already exists. Please select another one."
    assert get_casebyname("testnotuse1") == get_casebyname("testnotuse1")
    assert delete_case("testnotuse1") == "OK"
