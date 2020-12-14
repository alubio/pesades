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
Cases info module
"""
from datetime import datetime
from yaml import full_load, dump
from devices_ds import thisdevice

cases = []
"""List of cases"""

class Case():
    """Case information"""
    def __init__(self, name, id_external, description, notary_name, notary_phone, notary_email, isthisdevice):
        """Initializer"""
        self.name = name
        """Name of the case"""
        self.id_external = id_external
        """Unique external ID of the case"""
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
        """Pictures from the crime scene"""
        self.evidence_sm = []
        """Storage medias available for storing evidences"""
        self.case_sm = []
        """Storage medias from case"""
        if isthisdevice:
            self.devices.append(thisdevice)

        # Append newly created case to cases list
        cases.append(self)

    def addthisdevice(self):
        self.devices.append(thisdevice)

    def delthisdevice(self):
        self.devices.remove(thisdevice)

def get_listcasenames():
    listcasenames = []
    for case in cases:
        listcasenames.append(case.name)
    return listcasenames

def get_casebyname(name):
    for case in cases:
        if name == case.name:
            return case

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

def store_case(name, id_external, description, notary_name, notary_phone, notary_email, isthisdevice):
    """Store a new case"""
    # Check not duplicate name
    for case in cases:
        if name == case.name:
            return "Case name already exists. Please select another one."
    # Check not duplicate id
    for case in cases:
        if id_external == case.id_external:
            return "Case ID already exists. Please select another one."
    newcase = Case(name, id_external, description, notary_name, notary_phone, notary_email, isthisdevice)
    save_cases()
    return "OK"

def delete_case(name):
    for case in cases:
        if name == case.name:
            cases.remove(case)
            save_cases()
            return "OK"
    return "Case does not exist"

def update_case(old_name, name, id_external, description, notary_name, notary_phone, notary_email, isthisdevice):
    """Update a case"""
    # Remove old case
    result = delete_case(old_name)
    if result == "OK":
        # Store new updated case
        result = store_case(name, id_external, description, notary_name, notary_phone, notary_email, isthisdevice)
        if result == "OK":
            save_cases()
        else:
            result = result + " Case store operation in update failed. Cases information is inconsistent."
    else:
        result = "Case does not exist. Update failed."
    return result
