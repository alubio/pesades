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
basicConfig(filename='src/ds/session.log', format='%(asctime)s:session:%(levelname)s:%(message)s', level=INFO, datefmt="%Y-%m-%dT%H:%M:%S%z")
from operators_ds import load_operators
from cases_ds import load_cases
from datetime import datetime
from pesades_aux import stringsinshellexec, shellexec
from pesades_config import NTPserver1, NTPserver2, ipath

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
        logentry = str(datetime.utcnow().isoformat())+": "+message
        self.sessionlog.append(logentry)
        # TODO self.case.log(logentry)
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
            fsession.log("Wiped "+disk)
    r,o,e = shellexec("parted -s -m -a optimal "+disk+" mklabel gpt")
    if r != 0:
        fsession.log("Problem creating GPT label in "+disk)
        fsession.log(e+o)
        return 0
    else:
        fsession.log("Created GPT label in "+disk)
    if format == 'ntfs':
        r,o,e = shellexec("parted -s -m -a optimal "+disk+" mkpart primary ntfs 0% 100%")
        if r != 0:
            fsession.log("Problem creating primary NTFS partition in "+disk)
            return 0
        else:
            fsession.log("Created primary NTFS partition in "+disk)
        import time
        time.sleep(2)
        if fast:
            r,o,e = shellexec("mkfs.ntfs -f -L "+label+" "+disk+"1")
        else:
            r,o,e = shellexec("mkfs.ntfs -L "+label+" "+disk+"1")
        if r != 0:
            fsession.log("Problem NTFS formatting "+disk+"1")
            return 0
        else:
            fsession.log("NTFS formatted "+disk+"1")
        time.sleep(2)
        r,o,e = shellexec("lsblk -n -o UUID "+disk+"1")
        if r != 0:
            fsession.log("Problem getting UUID of "+disk+"1. The disk should be formatted")
            return 0
        return o
    elif format == 'ext4':
        r,o,e = shellexec("parted -s -m -a optimal "+disk+" mkpart primary ext4 0% 100%")
        if r != 0:
            fsession.log("Problem creating primary ext4 partition in "+disk)
            return 0
        else:
            fsession.log("Created primary ext4 partition in "+disk)
        import time
        time.sleep(2)
        r,o,e = shellexec("mkfs.ext4 -L "+label+" "+disk+"1")
        if r != 0:
            fsession.log("Problem ext4 formatting "+disk+"1")
            return 0
        else:
            fsession.log("ext4 formatted "+disk+"1")
        time.sleep(2)
        r,o,e = shellexec("lsblk -n -o UUID "+disk+"1")
        if r != 0:
            fsession.log("Problem getting UUID of "+disk+"1. The disk should be formatted")
            return 0
        return o
    else:
        return 0

def acquire_disk(disk, dst, caseid, evidenceid, desc, operator, format='E01'):
    if format != 'E01' and format != '001':
        fsession.log("Unknown acquisition format")
        return False
    from os import path, mkdir, remove
    directory = dst+"/"+caseid
    fsession.log("Initiating acquisition of disk "+disk+" into "+directory)
    if not path.isdir(directory):
        try:
            mkdir(directory)
        except OSError:
            fsession.log("Problem acquiring disk "+disk+" into "+directory+
                            ". Failed to create the case directory.")
        else:
            fsession.log("Created directory "+directory+" to store evidence "+evidenceid)
    file = directory+"/"+evidenceid
    if format == "E01":
        if path.isfile(file+".E01"):
            fsession.log("Problem acquiring disk "+disk+" into "+directory+
                            ". The acquisition already exists")
            return False
    elif format == "001":
        if path.isfile(file+".001"):
            fsession.log("Problem acquiring disk "+disk+" into "+directory+
                            ". The acquisition already exists")
            return False
    fsession.log ("Calculating original pre hashes of "+disk)
    premd5 = md5sum(disk)
    fsession.log ("Original pre MD5 hash: "+premd5)
    presha1 = sha1sum(disk)
    fsession.log ("Original pre SHA1 hash: "+presha1)
    fsession.log ("Acquiring "+disk+" into "+directory)
    if format == 'E01':
        r,o,e = shellexec(ipath+"/SO/ftkimager "+disk+" "+file+" --quiet --e01 --compress 9"+
                           " --case-number "+caseid+
                           " --evidence-number "+evidenceid+
                           " --description "+desc+
                           " --examiner " +operator)
        if r != 0:
            fsession.log("Problem acquiring in E01 format of "+disk+" into "+directory)
            fsession.log(e)
            if path.isfile(file+".E01"):
                remove(file+".E01")
            if path.isfile(file+".E01.txt"):
                remove(file+".E01.txt")
            return False
        else:
            compmd5, compsha1 = get_computed_hashes(file+".E01.txt")
    elif format == 'RAW':
        r,o,e = shellexec(ipath+"/SO/ftkimager "+disk+" "+file+" --quiet")
        if r != 0:
            fsession.log("Problem acquiring in RAW format of "+disk+" into "+directory)
            fsession.log(e)
            if path.isfile(file+".001"):
                remove(file+".001")
            if path.isfile(file+".001.txt"):
                remove(file+".001.txt")
            return False
        else:
            compmd5, compsha1 = get_computed_hashes(file+".001.txt")
    else:
        return False
    
    fsession.log ("Image computed MD5 hash: "+compmd5)
    fsession.log ("Image computed SHA1 hash: "+compsha1)
    fsession.log ("Calculating original post hashes of "+disk)
    postmd5 = md5sum(disk)
    postsha1 = sha1sum(disk)
    fsession.log ("Original post MD5 hash: "+postmd5)
    fsession.log ("Original post SHA1 hash: "+postsha1)
    # Test hashes
    if premd5 == compmd5 == postmd5:
        if presha1 == compsha1 == postsha1:
            fsession.log("Disk "+disk+" acquired into "+directory)
            if format == "E01":
                if verify_acquisition(file+".E01.txt"):
                    return True
            elif format == "001":
                if verify_acquisition(file+".001.txt"):
                    return True
    # Hashes differ, advice and remove images
    if premd5 == postmd5:
        fsession.log("Problem acquiring disk "+disk+" into "+directory+". Hashes of the image differ from the original")
    else:
        fsession.log("Problem acquiring disk "+disk+" into "+directory+". The original disk has been modified !!!")
    if path.isfile(file+".E01"):
        remove(file+".E01")
    if path.isfile(file+".E01.txt"):
        remove(file+".E01.txt")
    if path.isfile(file+".001"):
        remove(file+".001")
    if path.isfile(file+".001.txt"):
        remove(file+".001.txt")
    return False

def acquire_file(src, dst, caseid, evidenceid, desc, operator):
    from os import path, mkdir, remove, stat
    directory = dst+"/"+caseid
    fsession.log("Initiating acquisition of file "+src+" into "+directory)
    start = datetime.utcnow()
    if not path.isdir(directory):
        try:
            mkdir(directory)
        except OSError:
            fsession.log("Problem acquiring file "+src+" into "+directory+
                            ". Failed to create the case directory.")
        else:
            fsession.log("Created directory "+directory+" to store evidence "+evidenceid)
    srcwopath = path.basename(src)
    file = directory+"/"+srcwopath
    if path.isfile(file):
        fsession.log("Problem acquiring file "+src+" into "+directory+
                        ". The acquisition already exists")
        return False
    # Check file type of the new file. We can only process regular files,
    # no directories or special files allowed.
    if not path.isfile(src):
        fsession.log("File doesn't exist or not a regular file "+src)
        return False
    fsession.log ("Calculating original pre hashes of "+src)
    premd5 = md5sum(src)
    fsession.log ("Original pre MD5 hash: "+premd5)
    presha1 = sha1sum(src)
    fsession.log ("Original pre SHA1 hash: "+presha1)
    # Copy evidence preserving attributes if possible
    r,o,e = shellexec("cp --preserve=all "+src+" "+file)
    # Create txt file with acquisition info in ftkimager style
    with open (file+".txt", "w") as info:
        info.write("Case Information: "+"\n")
        info.write("Acquired using: cp"+"\n")
        info.write("Case Number: "+caseid+"\n")
        info.write("Evidence Number: "+evidenceid+"\n")
        info.write("Unique description: "+desc+"\n")
        info.write("Examiner: "+operator+"\n")
        info.write("Notes: "+"\n")
        info.write(""+"\n")
        info.write("--------------------------------------------------------------"+"\n")
        info.write(""+"\n")
        info.write("Information for "+path.abspath(src)+":\n")
        info.write(""+"\n")
        info.write("[File Attributes]"+"\n")
        st = stat(src)
        print(st)
        info.write("Size:  "+str(st.st_size)+"\n")
        info.write("UID:   "+str(st.st_uid)+"\n")
        info.write("GID:   "+str(st.st_gid)+"\n")
        info.write("Last Modification Time:                "+datetime.fromtimestamp(st.st_mtime).ctime()+"\n")
        info.write("Last Access Time:                      "+datetime.fromtimestamp(st.st_atime).ctime()+"\n")
        info.write("Creation or Last metadata change Time: "+datetime.fromtimestamp(st.st_ctime).ctime()+"\n")
        info.write("Mode:                                  "+stat.filemode(st.st_mode)+"\n")
        # TODO
        info.write(""+"\n")
        info.write("[Computed Hashes]"+"\n")
        info.write(" MD5 checksum:  "+premd5+"\n")
        info.write(" SHA1 checksum: "+presha1+"\n")
        info.write(""+"\n")
        info.write("Image Information:"+"\n")
        info.write(" Acquisition started:  "+start.ctime()+"\n")
        info.write(" Acquisition finished: "+datetime.utcnow().ctime()+"\n")

    fsession.log ("Calculating original post hashes of "+src)
    postmd5 = md5sum(src)
    postsha1 = sha1sum(src)
    fsession.log ("Original post MD5 hash: "+postmd5)
    fsession.log ("Original post SHA1 hash: "+postsha1)
    fsession.log ("Calculating acquired evidence hashes in "+file)
    compmd5 = md5sum(file)
    compsha1 = sha1sum(file)
    fsession.log ("Acquired MD5 hash: "+compmd5)
    fsession.log ("Acquired SHA1 hash: "+compsha1)
    # Test hashes
    if premd5 == postmd5 == compmd5:
        if presha1 == postsha1 == compsha1:
                fsession.log("File "+src+" acquired into "+directory)
            return True
    # Hashes differ, advice and remove images
    if premd5 == postmd5:
        fsession.log("Problem acquiring file "+src+" into "+directory+". Hashes of the acquired file differ from the original")
    else:
        fsession.log("Problem acquiring file "+src+" into "+directory+". The original file has been modified !!!")
    if path.isfile(file):
        remove(file)
    if path.isfile(file+".txt"):
        remove(file+".txt")
    return False

def verify_acquisition(file):
    r,o,e = shellexec(ipath+"/SO/ftkimager --verify "+file)
    if r != 0:
        fsession.log("Problem verifying acquisition in "+file)
        fsession.log(o)
        return False
    else:
        fsession.log("Verified acquisition in "+file)
        return True

def md5sum(file):
    r,o,e = shellexec("md5sum "+file)
    if r != 0:
        fsession.log("Problem calculating MD5 hash from "+file)
        fsession.log(e)
        return 0
    else:
        return o.strip().split(' ')[0]

def sha1sum(file):
    r,o,e = shellexec("sha1sum "+file)
    if r != 0:
        fsession.log("Problem calculating SHA1 hash from "+file)
        fsession.log(e)
        return 0
    else:
        return o.strip().split(' ')[0]

def get_computed_hashes(file):
    with open(file) as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if "Computed Hashes" in lines[i]:
                return lines[i+1].strip().split(' ')[5], lines[i+2].strip().split(' ')[4]

if __name__ == "__main__":
    print(acquire_file("LICENSE", "/media/sdb1", "case12", "ev14", "desc", "opera")) 
