'''
Config
'''

import random

class Config(object):

	def __init__(self):
		
		self.baseSize = 1024
		
		self.minStorage = 10
		self.maxStorage = 15
		
		self.minFile = 1
		self.maxFile = 5
		
		self.minAccess = 0.5
		self.maxAccess = 3.0
		
		self.safeFilesPerStorage = self.minStorage / self.maxFile
		self.storages = 10
		
	def nextStorageSize(self):
		return random.randint(self.minStorage, self.maxStorage) * self.baseSize
	
	def nextFileSize(self):
		return random.randint(self.minFile, self.maxFile) * self.baseSize
	
	def nextAccessTime(self):
		return random.uniform(self.minAccess, self.maxAccess)
	