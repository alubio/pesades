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
PESADES discovery engine.
"""
#from blkinfo import *
from pyudev import *

def test_blkinfo():
    myblkd = BlkDiskInfo()
    all_my_disks = myblkd.get_disks()
    for disk in all_my_disks:
        #print(disk['name'],disk['mountpoint'],disk['tran'],disk['vendor'], disk['model'], disk['statistics'])
        print (disk)

    print (all_my_disks[1].keys())
    # lsblk -n -l -o PATH,MOUNTPOINT,TYPE

def test_pyudev():
    context = Context()
    ignoredevices = ["loop", "ram", "nbd", "vbox"]
    for device in context.list_devices(subsystem='block', DEVTYPE='disk'):
        devname = device.properties['DEVNAME']
        if not any([x in devname for x in ignoredevices]):
            idmodel = device.get('ID_MODEL')
            idserialshort = device.get('ID_SERIAL_SHORT')
            idvendor = device.get('ID_VENDOR')
            #for key in device.properties.keys():
            #    print (key, device.properties[key])
            print (devname, idvendor, idmodel, idserialshort)

if __name__ == "__main__":
    print()
    test_pyudev()
    print()
