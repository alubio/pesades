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
PESADES auxiliary functions.
"""

def shellexec(command):
    """Function to execute command on a shell"""
    # TODO not threading
    import subprocess
    import shlex
    returncode=1
    output=""
    errors=""
    with open('tempstdout.txt','w+') as fout:
        with open('tempstderr.txt','w+') as ferr:
            try:
                returncode = subprocess.call(shlex.split(command),stdout=fout,stderr=ferr)
                fout.seek(0)
                output = fout.read()
                ferr.seek(0) 
                errors = ferr.read()
            except:
                returncode=1
                output=""
                errors=""
    import os
    if os.path.exists("tempstdout.txt"):
        os.remove("tempstdout.txt")
    if os.path.exists("tempstderr.txt"):
        os.remove("tempstderr.txt")
    return returncode, output, errors

def stringsinshellexec(command, stringlist):
    """Returns True if all strings in the strings list are in the stdout from command"""
    returncode, output, errors = shellexec(command)
    if returncode == 0:
        for string in stringlist:
            if not string in output:
                return False
        return True
    else:
        return False
        