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
        self.operator = None
        """Operator in charge of the investigation"""
        self.case = None
        """Case in use"""
        self.sessionlog = []
        """Session log"""

        # Empty session log file
        # TODO rotate log file, create new one with different name
        open('src/ds/session.log', 'w').close()

    def log(self, message):
        """Log session messages into session logging file"""
        self.sessionlog.append(str(datetime.now())+": "+message)
        info(message)

    def set_case(self, casename):
        """Sets active case"""
        self.case = casename
        if not casename:
            self.log("No case in use")
        else:
            self.log("Case \""+casename+"\" in use")

    def updatesystemtime(self):
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
                break
            r,o,e = shellexec("timedatectl set-ntp true")
            if r != 0:
                self.log("ERROR Failed to activate NTP")
                break
            self.log("NTP configuration corrected")
        except:
            break
        self.log("ERROR updating system time and date")

    def start(self):
        """Session starting activities"""
        self.log("Update system time")
        self.updatesystemtime()
        self.log("Load operators from file")
        load_operators()
        self.log("Load cases from file")
        load_cases()
        self.log("Session started")

    def end(self):
        """Session ending activities"""
        self.log("Session ended")
