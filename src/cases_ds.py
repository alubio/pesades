# -*- coding: utf-8 -*-
"""
Cases info module
"""
from datetime import datetime

last_id = 1
"""Last ID used"""
cases = []
"""List of cases"""

class Case():
    """Case information"""
    def __init__(self, name, description):
        """Initializer"""
        global last_id
        self.name = name
        """Name of the case"""
        self.id = last_id
        last_id += 1
        """Unique ID of the case"""
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

a = Case ("sdsd", "2323")
print (a.id)
print (last_id)
b = Case ("sdsd", "2323")
print (b.open_date)
print (last_id)

