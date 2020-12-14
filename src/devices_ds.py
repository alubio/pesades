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
Devices info module: pen drives, PCs, laptops, etc.
"""

DeviceTypes = ['computer', 'laptop', 'usbpendrive', 'CD', 'DVD', 'NAS', 'smartphone']
"""Predefined device types"""

class Device():
    """Device information"""
    def __init__(self, name, type, description, manufacturer, model, serial):
        """Initializer"""
        self.name = name
        """Name of the device"""
        self.type = type
        """Type: PC, laptop, usbpendrive, CD, DVD, NAS, smartphone"""
        self.description = description
        """Description of the device"""
        self.manufacturer = manufacturer
        """Manufacturer of the device"""
        self.model = model
        """Model string of the device"""
        self.serial = serial
        """Serial number"""

# Define special predefined devices
thisdevice = Device('This device', 'computer','The device where PESADES is running', 'Unknown', 'Unknown', 'Unknown')
