# Pancakes Class
class Pancakes:

	# Constructor
	def __init__(self, stack):
		self.stack = stack
		self.g_cost = 0
		self.h_cost = self.heuristic()
		self.f_cost = self.g_cost + self.h_cost

	# Overload '<' operator for use in Priority Queue
	def __lt__(self,other):
		return self.f_cost < other.f_cost

	# Prints the current stack
	def print_st(self, done = False, initial = False):
		st = " ".join([str(i) for i in self.stack])
		if (done):
			print(("Final Stack:  " + st).rjust(31))
		elif(initial):
			print(("Initial Stack:  " + st).rjust(31))
		else:
			print(("Flip Stack:  "+ st).rjust(31))
			

	# Checks if we have reached the goal
	def goal_reached(self):
		st = self.stack
		return all(st[i] >= st[i + 1] for i in range(len(st)-1))

	# Flip function -- reverse order of the first k + 1 pancakes
	def flip(self, k):
		i = 0
		while(i < k):
			temp = self.stack[i]
			self.stack[i] = self.stack[k]
			self.stack[k] = temp
			k -= 1
			i += 1

	# Gap Heuristic -- used as the forward cost function
	def heuristic(self):
		st = self.stack
		h = 0
		for i in range(len(st)-1):
			if (abs(st[i+1] - st[i]) > 1):
				h += 1
		return h


