class Queue():
	def __init__(self):
		self.l = []
	def enqueue(self,val):
		self.l.append(val)
	def dequeue(self):
		self.l.pop(0)
	def show(self):
		for i in self.l:
			if i<10:
				print('|__',i,'__',end='|')
			else:
				print('|_',i,'__',end='|')
		print('')
			
