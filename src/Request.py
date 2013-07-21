'''
Request & subclasses
'''

class Request(object):

	def __init__(self, typ, ID):
		self.type = typ
		self.ID = ID
		self.metadata = None
		self.accessTime = 0