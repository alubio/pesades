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
		open('src/ds/session.log', 'w').close()

	def log(self, message):
		"""Log session messages into session logging file"""
		self.sessionlog.append(message)
		info(message)
