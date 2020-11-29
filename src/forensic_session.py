# -*- coding: utf-8 -*-
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
		self.sessionlog = []
		"""Session log"""

		# Empty session log file
		open('src/ds/session.log', 'w').close()

	def log(self, message):
		"""Log session messages into session logging file"""
		self.sessionlog.append(message)
		info(message)
