'''
entry-point
'''

from StorageSystem import StorageSystem
from Request import Request
import threading

if __name__ == '__main__':
	print "main:", threading.currentThread().getName()
	system = StorageSystem()
	system.run()
	
	for i in xrange(30):
		system.makeRequest(Request("new", 0))
		
	for i in xrange(20):
		system.makeRequest(Request("read", system.randomID()))
	
	print "main done! - test 2"
