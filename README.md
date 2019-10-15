# Pancake Problem
Ben London

An A* and UCS implementation applied to the Pancake Problem.

Ran and tested on Python 3.7.1 using command:
	`python3 astar.py`
	OR
	`python3 ucs.py`

Description:

astar.py and ucs.py contain implementations of the A* algorithm and
the Uniformed Cost Search algorithm respectively. Both algorithms 
are run on the classic "pancake problem", defined as follows:
	A messy cook has a disordered stack of 5 differently-sized pancakes
	[size from 1 to 5] and a spatula that can be inserted at any point 
	in the stack and used to flip all pancakes above it. The goal is 
	for the cook to have them in the “correct” order for the customer, 
	that is, the large on the bottom up to the smallest on top 
	([5, 4, 3, 2, 1]). 
