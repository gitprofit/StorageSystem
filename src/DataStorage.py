'''
DataStorage
'''

import threading
import time
from RequestQueue import RequestQueue
from Logger import Logger

class DataStorage(threading.Thread):

	def __init__(self, storageSize):
		threading.Thread.__init__(self)
		
		self.logger = Logger()
		
		self.files = dict()
		self.requests = RequestQueue()
		
		self.totalSpace = storageSize
		self.usedSpace = 0
		self.freeSpace = storageSize
		
	def reserve(self, size):
		self.freeSpace -= size
		self.usedSpace += size
		
	def free(self, size):
		self.freeSpace += size
		self.usedSpace -= size
	
	def run(self):
		while True:
			request = self.requests.take()
			self.processRequest(request)
	
	def addRequest(self, request):
		# scheduler will be called here
		self.requests.lock.acquire()
		self.requests.data.append(request)
		self.requests.lock.notifyAll()
		self.requests.lock.release()

	def processRequest(self, request):
		self.logger.log("request processing: " + request.type + ", file: " + str(request.ID))
		time.sleep(request.accessTime)
		self.logger.log("done processing")
		