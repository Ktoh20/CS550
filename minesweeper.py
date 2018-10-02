#minesweeper map

import sys
import random

row = []
collumn = []

w = int(sys.argv[1])
h = int(sys.argv[2])
b = int(sys.argv[3])

#corrected version of grid
i = [[0]*w for x in range(h)]
for x in i:
	print(*x)

#printing bombs
for i in range(b):
	y = random.randint(0, h)
	u = random.randint(0, w)
	for a in range(b):
		row.insert(u, "*")
		collumn.insert(y, "*")

#locating system
for i in range(b):
	if [x + 1] == "*":
		row.insert(1)
	elif [x - 1] == "*":
		row.insert(1)
	else:

#locating system for center not edges
for i in range(b):
	if [y + 1] == "*":
		collumn.insert(1)
	elif [y - 1] == "*":
		collumn.insert(1)
	else:
		row.index(x,"*")
	if [x + 1] and [y + 1] == "*":
		row.insert(2)
	elif [x - 1] and [y - 1] == "*":
		row.insert(2)
	elif [x -1] and [y + 1] == "*":
		row.insert(2)
	elif [x + 1] and [y - 1] == "*":
		row.insert(2)
	else:
		row.index(x,"*")

print(i)



