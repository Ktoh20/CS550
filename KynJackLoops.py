from __future__ import division
import random

jellybeans = 50
numDays = 0
students = 1
n = 3
b = 4

#1
for i in range(5):
    print(i)

#2
for x in range(5,11):
	y-=5
	print(y)
#3
for i in range(11):
	print(15-i)

#4
for x in range(11):
	y-=5
	print(y)

#5
for i in range(13):
	print(25 + 2*i)

for i in range(25):
	x = i + 25
	if x%2 != 0:
		print(x)

#6
for x in range(11):
	x**2
	print(x)

#7
#2
while x>5 and x<10:
	y-=5
	print(y)
#4
while x < 10:
	y-=5
	print(y)
#6
while x < 11:
	x**2
	print(x)

#7
#1
i = 0
while i < 5:
	print(i)
	i += 1

#3
i = 15
while i >= 5:
	print(i)
	i -= 1

#5
i = 0
while i<13:
	print(25 + 2*i)  
	i += 1

#7
i = 0
while i<25:
	x = i +25
	if x%2 != 0:
		print(x)
	i += 1


#8
while days < 58:
	days+=1
	z = 57-=days
	print(z)

# 9
while jellybeans>0:
	jellybeans = jellybeans - students - 2
	numDays += 1

#10 assuming x is already 14
for x in range(firstdayofvacation):
	z = firdayofvacation-=x
	print(z)
	x+=1

#11
def factorial(number):
	if number == 1:
		return 1
	return number *factorial(number-1)
result = factorial(n)


#12 
for x in range(distance):
	z = (x+24)//1
	print(z)

#13
exponent = 1
while b>0:
	exponent = exponent*n
	b -= 1


#14 
['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for x in range(len(list)+1):
	print(x)

#15
list1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for x in range(len(list1)):
	if x == 0 or x == 4 or  x==8 or x == 14 or x == 20 or x == 24:
		print(str(list1[x])+ ' is a vowel')
	else:
		print(str(list1[x]) +' is a consonant')


#16
for x in range(11):
	print(x)
	for y in range(11):
		print(y)

#17
for i in range(2, 21):
	num = 1/i
	print("1/" +str(i) +" = " + str(float(num)))

#18
#there is a list of all the numbers from 1-100
while x < 101:
	x = list[x]+x
	print(x)
	x+1

#19 - They are correct
dem = 1
PI = 0
sign = 1
n = 10000
for x in range(n):
	PI = PI + sign*(1/dem)
	sign = -1*sign
	dem = dem +2
PI = 4 * PI
print(PI)

#20
mothers = 1
newMothers = 0
years = 5
population = 1
for x in range(years):
	for q in range(mothers):
		t = 12*(random.randint(1,14))
		population = population + t
		newMothers = newMothers + t//2
	mothers = mothers + newMothers

print(population)


21
years = 5
population = 1
for c in range(1000):
	mothers = 1
	newMothers = 0
	years = 5

	for x in range(years):
		t = 12*(random.randint(1,14)) * mothers
		population = population + t
		newMothers = newMothers + t//2
		mothers = mothers + newMothers
avgpop = population/1000
print(avgpop)



#22
z = coza
b = loza
n = wowza
m = cozaloza
global x
list = [[0]*11 for i in range(111)]
while x < 111:
	if x % 3 ==0 and x % 5 == 0:
		list.len(0+x) = m
	elif x % 3 == 0:
		list.len(0+x) = z
	elif x % 5 == 0:
		list.len(0+x) = b
	elif x % 7 == 0:
		list.len(0+x) = n
	else:
		list.len(0+x) = x
	x+=1
print(list)

#23

list1 = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]
list2 = ['*', '|', 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(len(list1)):
	for q in range (9):
		z = q + 1
		list1[x].insert(z,list1[x][0]*z)
	list1[x].insert(1, '|')
print(*list2)
print('------------------------------')
for x in list1:
	print(*x)

#24
board1 = [[" "]*7 for i in range(7)]
global bx
global by
global bm
global bn
global bp
global bo
bx = 0
by = 0
bm = 0
bn = 0
for x in range(8):
	bx+=1
	board1[by][bx]="#"
for y in range(8):
	by+=1
	board1[by][0]="#"
for z in range(8):
	bx-=1
	board1[by][bx] = "#"
for z in range(8):
	by-=1
	board1[by][bx] = "#"
for i in range (1,len(board)-1):
		for j in range(1,len(board1[0])-1):
			print(board1[i][j],end=" ")
		print("")
	print('-'*20)

board2 = [[" "]*7 for i in range(7)]
for l in range(8):
	bm+=1
	board2[bn][bm]="#"
for m in range(8):
	bm-=1
	board2[7][bm] = "#"
for j in range(8):
	bm +=1
	bn +=1
	board2[bn][bm] = "#"
bk = 7
bc = 0
for k in range(8):
	bk -= 1
	bc +=1
	board2[bc][bk] = "#"
for i in range (1,len(board2)-1):
		for j in range(1,len(board[0])-1):
			print(board2[i][j],end=" ")
		print("")
	print('-'*20)

bz = 0
bp = 0
board3 = board1
for z in range(8):
	bz+=1
	bp+=1
	board3[bz][bp] = "#"
bt = 7
bg = 0
for a in range(8):
	bt-=1
	bg+=1
	board3[bt][bg] = "#"
for i in range (1,len(board3)-1):
		for j in range(1,len(board[0])-1):
			print(board3[i][j],end=" ")
		print("")
	print('-'*20)

#25 - https://www.google.com/search?client=safari&rls=en&q=how+to+reverse+a+list+python&ie=UTF-8&oe=UTF-8
number = 15423
list1 = []
for z in str(number):
	list1.append(z)
list1.reverse()

print(*list1)




#26

