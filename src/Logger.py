'''
thread-safe IO-synchronized Logger
'''

import threading

class Logger(object):
	
	__shared_state = { }
	__lock = threading.RLock()

	def __init__(self):
		#self.__dict__ = self.__shared_state
		pass
	
	def log(self, msg):
		self.__lock.acquire()
		print threading.currentThread().getName(), ":", msg
		self.__lock.release()
	