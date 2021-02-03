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
PESADES expert system.
"""
from experta import *

# Facts
class ForensicSession(Fact):
    """
    Forensic session fact, there is only one. It defines properties related to the current session
    >>> ForensicSession(hurried=True)
    """
    hurried = Field(bool)
    # If the operator is in a hurry

class Case(Fact):
    """
    Case facts. They define properties related to the case
    >>> Case(name="case1", ext4=False)
    """
    name = Field(str, mandatory=True)
    # Name of the case
    ext3 = Field(bool)
    # If the forensic analyst requires the use of ext4 in the evidence storage drives

class Storage(Fact):
    """
    Storage medias facts
    >>> Storage(name="storage1", freespace=0)
    """
    name = Field(str, mandatory=True)
    # Name of the storage
    freespace = Field(int)
    # Free space available for storing evidences

class Evidence(Fact):
    """
    Evidences acts
    >>> Evidence(name="evidence1", dvr=False, device=True, size=0)
    """
    name = Field(str, mandatory=True)
    # Name of the evidence
    dvr = Field(bool)
    # If the evidence is a disk from a DVR system
    device = Field(bool)
    # If the evidence is a device that contains storage that should be processed. Otherwise is a piece of data or information
    size = Field(int)
    # Size of the evidence in the disk

# Expert system
class ForensicExpert(KnowledgeEngine):
   
    """
    Forensic session decision rules
    """
    
    # Raw format if the operator is in a hurry and there is enough space
    @Rule(ForensicSession(hurried=True),
          Evidence(name=MATCH.name))
    def hurried_enoughspace(self, name):
        print("raw para evidencia "+name)

    """
    Case decision rules
    """
    
    # Ext4 format for storage media if forensic analyst requires it
    @Rule(Case(ext4=True),
          Storage(name=MATCH.name))
    def ext4(self, name):
        print("ext4 para almacenamiento "+name)

    # No evidence storage medias
    @Rule(NOT(Storage()),Evidence())
    def no_storage(self):
        print("Evidencias pendientes de procesar, solicitar dispositivos de almacenamiento de evidencias")

    """
    Evidence processing rules
    """
    
    # No pending evidences
    @Rule(NOT(Evidence()))
    def no_evidence(self):
        print("No hay evidencias pendientes.")

    # Search for virtual drives in devices
    @Rule(Evidence(name=MATCH.name,
                   device=True),
          salience=1)
    def search_virtualdrives(self, name):
        print("Buscar virtual drives en evidencia "+name)

    # Not enough free space on storage
    @Rule(Evidence(name=MATCH.ename,
                   size=MATCH.size),
          Storage(name=MATCH.sname,
                  freespace=MATCH.freespace),
          TEST(lambda size, freespace: freespace < size))
    def not_enough_storage(self, ename, sname):
        print("Almacenamiento insuficiente en almacen "+sname+" para almacenar evidencia "+ename+", solicitar dispositivos de almacenamiento de evidencias.")

    # Ask operator if the new device evidence is a DVR disk TODO
    @Rule(Evidence(name=MATCH.name, device=True),
    	  NOT(Evidence(dvr=W())),
    	  salience=1)
    def ask_if_dvr(self, name):
    	print("¿el disco "+name+" es de un DVR?")

    # Raw format for DVR disks if there is enough space on a storage
    @Rule(Evidence(name=MATCH.ename,
                   size=MATCH.size,
                   dvr=True),
          Storage(name=MATCH.sname,
                  freespace=MATCH.freespace),
          TEST(lambda size, freespace: freespace > size),
          salience=1)
    def dvr_enoughspace(self, ename, sname, size, freespace):
        print("raw para evidencia DVR "+ename+" "+str(freespace)+" > "+str(size)+" en almacenamiento "+sname)

    # Process evidence
    @Rule(Evidence(name=MATCH.ename,
                   size=MATCH.size),
          Storage(name=MATCH.sname,
                  freespace=MATCH.freespace),
          TEST(lambda size, freespace: freespace > size))
    def process_evidence(self, ename, sname, size, freespace):
        print("Procesar evidencia "+ename+" en almacenamiento "+sname)
        procesa_evidencia(ename, sname, size, freespace)



if __name__ == "__main__":
    # Development testing code, pleaase ignore
    evidencias={}
    almacenes={}

    def procesa_evidencia(evidencia, almacen, tamaño, espacio):
        global engine
        print("Evidencia "+evidencia+" procesada en almacen "+almacen)
        engine.retract(evidencias[evidencia])
        del evidencias[evidencia]
        engine.retract(almacenes[almacen])
        del almacenes[almacen]
        almacenes[almacen] = engine.declare(Storage(name=almacen, freespace=espacio-tamaño))
        print("Espacio libre en almacen "+almacen+": "+str(espacio-tamaño))

    engine = ForensicExpert()
    engine.reset()
    engine.declare(ForensicSession(hurried=False))
    engine.declare(Case(name="case1", ext4=False))
    engine.run()
    print("1-------------")
    evidencias["evidence1"] = engine.declare(Evidence(name="evidence1", size=3000))
    engine.run()
    print("2-------------")
    almacenes["storage1"] = engine.declare(Storage(name="storage1", freespace=6002))
    engine.run()
    print("3-------------")
    almacenes["storage2"] = engine.declare(Storage(name="storage2", freespace=3000))
    engine.run()
    print("4-------------")
    evidencias["evidence2"] = engine.declare(Evidence(name="evidence2", dvr=True, device=True, size=3001))
    evidencias["evidence3"] = engine.declare(Evidence(name="evidence3", device=True, size=2000))
    evidencias["evidence4"] = engine.declare(Evidence(name="evidence4", size=30))
    engine.run()
    print("5-------------")
    evidencias["evidence5"] = engine.declare(Evidence(name="evidence5", device=True, size=301))
    engine.run()
    evidencias["evidence6"] = engine.declare(Evidence(name="evidence6", device=True, size=3001))
    engine.run()