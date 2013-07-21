'''
thread-safe random-access RequestQueue
'''

import threading

class RequestQueue(object):

	def __init__(self):
		self.data = list()
		self.lock = threading.Condition()
		
	def take(self):
		self.lock.acquire()
		while len(self.data) == 0:
			self.lock.wait()
		item = self.data.pop(0)
		self.lock.release()
		return item