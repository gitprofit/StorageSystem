'''
File & FileMetadata
'''

import datetime

class File(object):

	def __init__(self, metadata):
		self.ID = metadata.ID
		self.metadata = metadata



class FileMetadata(object):

	def __init__(self):
		self.ID = 0
		self.name = "empty.name"
		self.size = 0
		self.lastAccess = datetime.datetime.now()
		self.location = None