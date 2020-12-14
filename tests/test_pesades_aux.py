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
Tests for pesades_aux.py module.
"""

from pesades_aux import *

def test_shellexec():
    assert shellexec("echo hola") == (0,'hola\n','')
    assert shellexec("commandnotexists") == (1,'','')

def test_stringsinshellexec():
    assert stringsinshellexec("echo hola adios", ["hola"]) == True
    assert stringsinshellexec("echo hola adios", ["hola","adios"]) == True