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
Evidences info module: pen drives, PCs, laptops, URLs, data, etc.
"""
from pesades_aux import shellexec

evidence_type = ["FILE", "DATA", "PICTURE", "DEVICE", "OTHER"]
"""Predefined evidence types"""
method_type = ["ACQUISITION", "COLLECTION"]
"""Predefined process method types"""

class Evidence():
    """Evidence information"""
    def __init__(self, name, type, description):
        """Initializer"""
        self.name = name
        """Name of the device"""
        self.description = description
        """Description of the device"""

device_type = ["PEN_DRIVE", "HARD_DRIVE", "DVR_HARD_DRIVE", "VIRTUAL_DRIVE", "CD", "DVD", "LAPTOP", "COMPUTER", "MOBILE_DEVICE", "OTHER"]
"""Predefined device types"""

class Device(Evidence):
    """Device information"""
    def __init__(self, name, description, evidence_type, device_type, manufacturer, model, serial, filename=""):
        super().__init__(name, evidence_type, description)
        self.filename = filename
        """Name of the system file /dev/xxx"""
        self.type = type
        """Type: PC, laptop, usbpendrive, CD, DVD, NAS, smartphone"""
        self.manufacturer = manufacturer
        """Manufacturer of the device"""
        self.model = model
        """Model string of the device"""
        self.serial = serial
        """Serial number"""

# Define special predefined devices
# TODO poner el hostname en el thisdevice
thisdevice = Device(shellexec("hostname")[1].rstrip(), 'The device where PESADES is running', 'DEVICE', 'COMPUTER', 'NA', 'NA', 'NA')