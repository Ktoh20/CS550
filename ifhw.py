import sys
x = float(sys.argv[1])
if x <= 5:
	if x <= 1.5:
		print("F")
	if x >= 1.5 and x < 2:
		print("D") 
	if x >= 2 and x < 2.5:
		print("D+")
	if x >= 2.5 and x < 2.85:
		print("C-")
	if x >= 2.85 and x < 3.2:
		print("C")
	if x >= 3.2 and x < 3.5:
		print("C+")
	if x >= 3.5 and x < 3.85:
		print("B-")
	if x >= 3.85 and x < 4.2:
		print("B")
	if x >= 4.2 and x < 4.5:
		print("B+")
	if x >= 4.5 and x < 4.7:
		print("A-")
	if x >= 4.7 and x < 4.85:
		print("A")
	if x >= 4.85 and x <= 5:
		print("A+")
else:
	print("you are obviously not looking at the instructions,goodbye")
