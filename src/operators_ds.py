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
Operators info module
"""
from datetime import datetime
from yaml import load, dump, Loader
from pesades_crypto import is_passwordok

operators = []
"""List of operators"""

class Operator():
    """Operator information"""
    def __init__(self, username, fullname, organization, role, phone, email, password):
        """Initializer"""
        self.username = username
        """Operator's username"""
        self.fullname = fullname
        """Operator's fullname"""
        self.create_date = datetime.utcnow()
        """Create date of the operator"""
        self.organization = organization
        """Operator's organization"""
        self.role = role
        """Operator's role"""
        self.phone = phone
        """Operator's phone number"""
        self.email = email
        """Operator's email"""
        self.password = password
        """Operator's hashed password"""

        # Append newly created operator to operators list
        operators.append(self)

def check_userpassword(username, password):
    global operators
    for operator in operators:
        if username == operator.username:
            if is_passwordok(password, operator.password):
                return True
    return False

def save_operators():
    """Write operators list to file"""
    global operators
    try:
        with open("src/ds/operators.yaml", 'w+') as file:
            dump(operators, file)
    except:
        # TODO Manage exception
        print ("ERROR: operators_ds: save_operators")
        return

def load_operators():
    """Read operators list from file"""
    global operators
    try:
        with open("src/ds/operators.yaml") as file:
            operators = load(file, Loader=Loader)
            if not operators:
                operators = []
    except Exception as e:
        # TODO Manage exception
        print ("ERROR: operators_ds: load_operators"+str(e))
        return

def store_operator(username, fullname, organization, role, phone, email, password):
    """Store a new operator"""
    global operators
    # Check not duplicate username
    for operator in operators:
        if username == operator.username:
            return "Username already exists. Please select another one."
    Operator(username, fullname, organization, role, phone, email, password)
    save_operators()
    return "OK"
