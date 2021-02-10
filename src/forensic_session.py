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
PESDES forensic specific classes.
"""

from logging import basicConfig, info, INFO
basicConfig(filename='src/ds/session.log', format='%(asctime)s:session:%(levelname)s:%(message)s', level=INFO)
from operators_ds import load_operators
from cases_ds import load_cases
from datetime import datetime
from pesades_aux import stringsinshellexec, shellexec
from pesades_config import NTPserver1, NTPserver2

class ForensicSession():
    """Forensic session management"""
    def __init__(self):
        """Initializer"""
        self.case = None
        """Case in use"""
        self.operator = None
        """Operator in charge of the investigation"""
        self.sessionlog = []
        """Session log"""
        hurried = False
        """If the operator is in a hurry, for decision making"""

        # Empty session log file
        # TODO rotate log file, create new one with different name
        open('src/ds/session.log', 'w').close()

    def set_hurried(self, value=True):
        # The operator may be in a hurry
        self.hurried = value
    
    def log(self, message):
        """Log session messages into session logging file"""
        self.sessionlog.append(str(datetime.now())+": "+message)
        self.case.log(message)
        info(message)

    def set_case(self, casename):
        """Sets active case"""
        self.case = casename
        if not casename:
            self.log("No case in use")
        else:
            self.log("Case \""+casename+"\" in use")

    def update_system_time(self):
        """Update system time and date"""
        if stringsinshellexec("timedatectl show-timesync",[NTPserver1, NTPserver2]):
            self.log("NTP servers configured")
            if stringsinshellexec("timedatectl status",["System clock synchronized: yes","NTP service: active"]):
                self.log("NTP active and in sync")
                return
        try:
            self.log("Trying to correct NTP configuration")
            import os
            if os.path.exists("/etc/systemd/timesyncd.conf"):
                os.remove("/etc/systemd/timesyncd.conf")
            with open('/etc/systemd/timesyncd.conf','w') as ofh:
                ofh.write("[Time]\nNTP="+NTPserver1+"\nFallbackNTP="+NTPserver2+"\n")
            r,o,e = shellexec("systemctl restart systemd-timesyncd.service")
            if r != 0:
                self.log("ERROR Failed to restart systemd-timesyncd.service")
                return
            r,o,e = shellexec("timedatectl set-ntp true")
            if r != 0:
                self.log("ERROR Failed to activate NTP")
                return
            self.log("NTP configuration corrected")
        except:
            pass
        self.log("ERROR updating system time and date")

    def start(self):
        """Session starting activities"""
        self.log("Update system time")
        self.update_system_time()
        self.log("Load operators from file")
        load_operators()
        self.log("Load cases from file")
        load_cases()
        self.log("Session started")

    def end(self):
        """Session ending activities"""
        self.log("Session ended")

fsession = ForensicSession()
"""Forensic session related information"""

def wipe_disk(disk, level=0):
    """Wipes the disk"""
    if level == 0:
        # Wipe partition table with zeros
        shellexec("dd if=/dev/zero of="+disk+" bs=512 count=1")
        fsession.log("Wiped with zeros partition table of "+disk)
        return True
    elif level == 1:
        # Wipe all with zeros
        shellexec("dd if=/dev/zero of="+disk+" bs=64K")
        fsession.log("Wiped "+disk+" with zeros")
        return True
    elif level == 2:
        # Wipe all with random
        shellexec("dd if=/dev/urandom of="+disk+" bs=64K")
        fsession.log("Wiped "+disk+" with randomness")
        return True
    elif level == 3:
        # Wipe all with shred
        shellexec("shred "+disk)
        fsession.log("Hard wiped "+disk+" with shred")
        return True
    else:
        return False

def format_disk(disk, format='ntfs', label='PESADESRW', fast=True, wipe=True):
    """Formats de disk and returns the UUID, 0 if fails """
    shellexec("umount "+disk+"1")
    fsession.log("Umounted "+disk)
    if wipe:
        if not wipe_disk(disk, level=0):
            fsession.log("Problem wiping "+disk)
            return 0
        else:
            print("Wiped "+disk)
    if format == 'ntfs':
        r,o,e = shellexec("parted -s -m -a optimal "+disk+" mklabel gpt")
        if r != 0:
            fsession.log("Problem creating GPT label in "+disk)
            return 0
        else:
            fsession.log("Created GPT label in "+disk)
        r,o,e = shellexec("parted -s -m -a optimal "+disk+" mkpart primary ntfs 0% 100%")
        if r != 0:
            fsession.log("Problem creating primary NTFS partition in "+disk)
            return 0
        else:
            fsession.log("Created primary NTFS partition in "+disk)
        import time
        time.sleep(5)
        if fast:
            r,o,e = shellexec("mkfs.ntfs -f -L "+label+" "+disk+"1")
        else:
            r,o,e = shellexec("mkfs.ntfs -L "+label+" "+disk+"1")
        if r != 0:
            fsession.log("Problem NTFS formatting "+disk+"1")
            return 0
        else:
            fsession.log("NTFS formatted "+disk+"1")
        return True
    elif format == 'ext4':
        # TODO
        return 0
    else:
        return 0

if __name__ == "__main__":
    print(format_disk("/dev/sdg"))
