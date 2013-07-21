'''
StorageSystem
'''

from DataStorage import DataStorage
from File import FileMetadata
from Config import Config

import random

class StorageSystem(object):

	def __init__(self):
		
		self.__config = Config()
		
		self.__metadata = { }
		self.__indexer = 1000;
		self.__storages = [ DataStorage(self.__config.nextStorageSize()) for i in xrange(self.__config.storages) ]
		
		self.__handlers = {
							"new" : self.__handleNew,
							"del" : self.__handleDel,
							"read" : self.__handleGen,
							"write" : self.__handleGen
						}
		
	def run(self):
		for s in self.__storages: s.start()
		
	def makeRequest(self, request):
		self.__handlers[request.type](request)
		
	def randomID(self):
		return random.choice(self.__metadata.keys())
		
	def __handleGen(self, request):
		request.metadata = self.__metadata[request.ID]
		request.accessTime = self.__config.nextAccessTime()
		request.metadata.location.addRequest(request)
	
	def __handleDel(self, request):
		request.metadata = self.__metadata.pop(request.ID)
		request.accessTime = self.__config.nextAccessTime()
		request.metadata.location.free(request.metadata.size)
		request.metadata.location.addRequest(request)
		
	def __handleNew(self, request):
		
		size = self.__config.nextFileSize()
		storage = self.__preferredStorage(size)
		if storage is None: return
		
		self.__indexer += 1
		
		meta = FileMetadata()
		meta.ID = self.__indexer
		meta.name = "new.file"
		meta.size = size
		meta.location = storage
		meta.location.reserve(meta.size)
		
		self.__metadata[self.__indexer] = meta

		request.ID = self.__indexer
		request.metadata = meta
		request.accessTime = self.__config.nextAccessTime()
		request.metadata.location.addRequest(request)
	
	def __preferredStorage(self, requiredCapacity):
		allowed = filter(lambda storage: storage.freeSpace >= requiredCapacity, self.__storages)
		if len(allowed) == 0: return None
		return min(allowed, key = lambda storage: storage.usedSpace/float(storage.totalSpace))
		