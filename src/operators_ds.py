# -*- coding: utf-8 -*-
"""
Operators info module
"""
from datetime import datetime
from yaml import full_load, dump
from pesades_crypto import is_passwordok

operators = []
"""List of operators"""

class Operator():
    """Operator information"""
    def __init__(self, username, fullname, organization, phone, email, password):
        """Initializer"""
        self.username = username
        """Operator's username"""
        self.fullname = fullname
        """Operator's fullname"""
        self.create_date = datetime.now()
        """Create date of the operator"""
        self.organization = organization
        """Operator's fullname"""
        self.phone = phone
        """Operator's phone number"""
        self.email = email
        """Operator's fullname"""
        self.password = password
        """Operator's hashed password"""

        # Append newly created operator to operators list
        operators.append(self)

def check_userpassword(username, password):
    for operator in operators:
        if username == operator.username:
            if is_passwordok(password, operator.password):
                return True
    return False

def save_operators():
    """Write operators list to file"""
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
            operators = full_load(file)
    except:
        # TODO Manage exception
        print ("ERROR: operators_ds: load_operators")
        return

def store_operator(username, fullname, organization, phone, email, password):
    """Store a new operator"""
    # Check not duplicate username
    for operator in operators:
        if username == operator.username:
            return "Username really exist. Please select another one."
    Operator(username, fullname, organization, phone, email, password)
    save_operators()
    return "OK"

# Load operators from file at init time
load_operators()
