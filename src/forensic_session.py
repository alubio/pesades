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
Forensic specific classes.
"""

from logging import basicConfig, info, INFO
basicConfig(filename='src/ds/session.log', format='%(asctime)s:session:%(levelname)s:%(message)s', level=INFO)
from operators_ds import load_operators
from cases_ds import load_cases
from datetime import datetime

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

	def start(self):
		"""Session starting activities"""
		# TODO Update system date and time
		from time import sleep
		self.log("Load operators from file")
		load_operators()
		self.log("Load cases from file")
		load_cases()
		self.log("Session started")

	def end(self):
		"""Session ending activities"""
		self.log("Session ended")
