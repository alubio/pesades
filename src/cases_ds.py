# -*- coding: utf-8 -*-
"""
Cases info module
"""
from datetime import datetime
from yaml import full_load, dump

last_id = 1
"""Last ID used"""
cases = []
"""List of cases"""

class Case():
    """Case information"""
    def __init__(self, name, description, notary_name, notary_phone, notary_email):
        """Initializer"""
        global last_id
        self.name = name
        """Name of the case"""
        self.id = last_id
        last_id += 1
        """Unique ID of the case"""
        self.notary_name = notary_name
        """Notary or witness phone"""
        self.notary_phone = notary_phone
        """Notary or witness email"""
        self.notary_email = notary_email
        """Notary or witness of the case"""
        self.open_date = datetime.now()
        """Opening date of the case"""
        self.description = description
        """Description of the case"""
        self.devices = []
        """Known devices like pen drives, PCs, laptops, etc."""
        self.pictures = []
        """Pictures from the scrime scene"""
        self.evidence_sm = []
        """Storage medias available for storing evidences"""

        # Append newly created case to cases list
        cases.append(self)

def get_listcasenames():
    listcasenames = []
    for case in cases:
        listcasenames.append(case.name)
    return listcasenames

def save_cases():
    """Write cases list to file"""
    try:
        with open("src/ds/cases.yaml", 'w+') as file:
            dump(cases, file)
    except:
        # TODO Manage exception
        print ("ERROR: cases_ds: save_cases")
        return

def load_cases():
    """Read cases list from file"""
    global cases
    try:
        with open("src/ds/cases.yaml") as file:
            cases = full_load(file)
    except:
        # TODO Manage exception
        print ("ERROR: cases_ds: load_cases")
        return

def store_case(name, description, notary_name, notary_phone, notary_email):
    """Store a new case"""
    # Check not duplicate name
    for case in cases:
        if name == case.name:
            return "Case name really exist. Please select another one."
    Case(name, description, notary_name, notary_phone, notary_email)
    save_cases()
    return "OK"

# Load operators from file at init time
load_cases()
