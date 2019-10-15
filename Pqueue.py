import heapq

# Priority Queue Class
class PQ:

	def __init__(self):
		self.heap = []

	def push(self, priority, value):
		heapq.heappush(self.heap,(priority, value))
		

	def pop(self):
		return heapq.heappop(self.heap)


	def is_empty(self):
		return (len(self.heap) == 0)