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

def test_blkinfo():
    from blkinfo import BlkDiskInfo
    myblkd = BlkDiskInfo()
    all_my_disks = myblkd.get_disks()
    for disk in all_my_disks:
        #print(disk['name'],disk['mountpoint'],disk['tran'],disk['vendor'], disk['model'], disk['statistics'])
        print ("/dev/"+disk['name'], disk['vendor'], disk['model'], disk['serial'], str(round(int(disk['size'])/1000/1000/1000))+"GB", disk['tran'])
        #print (disk.keys())
        #print (disk)

    #print (all_my_disks[1].keys())
    # lsblk -n -l -o PATH,MOUNTPOINT,TYPE

def test_pyudev():
    from pyudev import Context
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

"""
Some useful linux commands:
cat /sys/block/sdb/device/model
cat /sys/block/sdb/device/vendor
lsblk --json -o SIZE,FSTYPE,LABEL,UUID,MOUNTPOINT /dev/sdb1
udevadm info --query=all --name=/dev/sda
blockdev --getsize64 /dev/sdf
sudo fdisk -l /dev/sda
sudo ./ftkimager --print-info /dev/sdb
"""
def get_disks():
    from pyudev import Context
    from blkinfo import BlkDiskInfo
    context = Context()
    myblkd = BlkDiskInfo()
    all_my_disks = myblkd.get_disks()
    ignoredevices = ["loop", "ram", "nbd", "vbox"]
    disks = []
    for device in context.list_devices(subsystem='block', DEVTYPE='disk'):
        name = device.properties['DEVNAME']
        if not any([x in name for x in ignoredevices]):
            model = device.get('ID_MODEL')
            serial = device.get('ID_SERIAL_SHORT')
            vendor = device.get('ID_VENDOR')
            size = ""
            transport = ""
            for disk in all_my_disks:
                if "/dev/"+disk['name'] == name:
                    size = str(round(int(disk['size'])/1000/1000))
                    transport = disk['tran']
                    break
            disks.append({"name":name, "vendor":vendor, "model":model, "serial":serial, "size":size, "transport":transport})
    return disks
