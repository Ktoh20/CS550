m = int(input("month:"))
d = int(input("day:"))
y = int(input("year:"))

yo = y - (14 - m) / 12
x = yo + (yo / 4) - (yo / 100) + (yo / 400)
mo = m + 12 * ((14-m) / 2) - 2
do = ((d + x + (31 * mo) / 12) % 7)//1

if do == 0:
	print("Sunday")
if do == 1: 
	print("Monday")
if do == 2:
	print("Tuesday")
if do == 3:
	print("Wednesday")
if do == 4:
	print("Thursday")
if do == 5:
	print("Friday")
if do == 6:
	print("Saturday")

