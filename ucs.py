import copy, heapq, random, os
from Pancakes import Pancakes 
from Pqueue import PQ


# Identical to astar expect f_cost = g_cost (astar is g_cost + h_cost)
def ucs(pancake_stack):

	#Initialize the frontier
	frontier = PQ()
	frontier.push(pancake_stack.g_cost, pancake_stack)

	all_paths = {}
	all_paths[pancake_stack] = None

	# Initialize list of visited nodes and their cost
	visited = []

	frontier_size = 0

	pancake_stack.print_st(initial = True)

	# Search through frontier
	while(not frontier.is_empty()):

		# Get lowest cost pancake stack from frontier
		curr = frontier.pop()[1]

		# If we have found the solution then return it
		if(curr.goal_reached()):
			final = curr
			n_flips = curr.g_cost

			path = [curr]

			# Gets path to solution
			while curr in all_paths:
				curr = all_paths[curr]
				if(curr == None):
					break
				path.append(curr)
				
			path.reverse()
			[i.print_st() for i in path[1:-1]]
			path[-1].print_st(done=True)
			return final, n_flips, frontier_size

		# For all possible flips, place them in the frontier
		for i in range(len(curr.stack)):
			frontier_stacks = [i[1] for i in frontier.heap]


			flip_copy = copy.deepcopy(curr)
			flip_copy.flip(i)

			# Update costs
			flip_copy.g_cost += 1
			flip_copy.f_cost = flip_copy.g_cost

			if(flip_copy in visited):
				continue
			# if child is not in the frontier or visited then insert child in frontier
			if (flip_copy not in frontier_stacks):
				all_paths[flip_copy] = curr
				frontier.push(flip_copy.g_cost, flip_copy)
				frontier_size += 1
				
			elif(flip_copy in frontier_stacks):
				x = frontier_stacks.index(flip_copy)
				curr_cost = frontier.heap[x][0]
				if(flip_copy.f_cost < curr_cost):
					frontier.heap[x][0] = flip_copy.f_cost
					heapq.heapify(frontier)

		visited.append(curr)





if __name__=='__main__':

	os.system('cls' if os.name == 'nt' else 'clear')
	print()
	print(("PANCAKE PROBLEM!").rjust(28))
	print("________________________________________")
	print()

	pancake_stack = [1, 2, 3, 4, 5]
	random.shuffle(pancake_stack)
	pancake_problem = Pancakes(pancake_stack)
	correct,flips, size = ucs(pancake_problem)

	print("________________________________________")
	print()
	print(("Flips needed: "+ str (flips)).rjust(27))
	print()
	print(("Number of nodes on frontier: "+str(size)).rjust(35))
	print("________________________________________")
	print()
		