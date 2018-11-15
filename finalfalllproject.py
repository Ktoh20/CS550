# Kyn Toh and Pearson Mewbourne maze
#make a path with 2 points
#make a path that connects the 2 points in the middle
#timer fucntion
#on my honor
#due november 15th (extension)
from PIL import Image 
import random as random
import math as m
import time
#decided to make it more gamelike, even though the maze can become much larger we thought that 7 by 7 was hard enough within 7 seconds
choice = int(input("Choose difficulity, (1-3) 1 = easy, 2 = medium, 3 = hard\n\n>>"))
if choice == 1:
	imgx = 5
if choice == 2:
	imgx = 6
if choice == 3:
	imgx = 7
imgy = imgx
#seconds
Sec = 0

#board generation (starts with a board of zeroes only)
board = [[0]*(imgx*2+2) for x in range(imgy*2+2)]
if imgx%2 == 0:
		vx = random.choice(range(0,imgx*2,2))
		vy = random.choice(range(0,imgx*2,2))
if imgx%2 == 1:
		vx = random.choice(range(1,imgx*2,2))
		vy = random.choice(range(1,imgx*2,2))
stop = 0

#this function is very important as it makes the maze stop from going over the limits
def stopfunc():
	global stop
	stop = 0
	for x in range(1,imgx*2+2):
		for y in range(1,imgy*2+2):
			if board[y][x] == 0:
				stop += 1
				print(stop)
	if stop > 0:
		if imgx%2 == 0:
			vx = random.choice(range(0,imgx*2+1,2))
			vy = random.choice(range(0,imgx*2+1,2))
		if imgx%2 == 1:
			vx = random.choice(range(0,imgx*2+1,2))
			vy = random.choice(range(0,imgx*2+1,2))
		blank(vx,vy)

#this was the code that generated the first occupied space in the maze
def blank(vx,vy):
	if vx-1 > 0 and vy-1>0:
		board[vx][vy] = " " 
		board[vx+1][vy+1] = "F"
		board[vx][vy+1] = "F"
		board[vx-1][vy+1] = "F"
		board[vx-1][vy] = "F"
		board[vx-1][vy-1] = "F"
		board[vx][vy-1] = "F"
		board[vx+1][vy-1] = "F"
		board[vx+1][vy] = "F"
	choice(vx,vy)

#this part was very hard to code as we had to run through many trials and errors, it basically prints the new free spaces in a recursive fashion
def choice(vx,vy):
	global count
	global up
	global down
	global left
	global right
	count = 0
	up, down, left, right = 0,0,0,0
	direction = random.randint(0,4)

	if vy+2<imgy:
		if direction == 1:
			count+=1
			board[vx][vy+2] = " "
			for i in range(-1,2,2):
				if vx+i > 0:
					board[vx+i][vy+2] = "F"
			board[vx][vy+3] = "F"
			down = 1
	else: 
		printo()

	if vy-2>0:
		if direction == 2:
			count+=1
			board[vx][vy-2] = " "
			for i in range(-1,2,2):
				if vx+i > 0:
					board[vx+i][vy-2] = "F"
			up = 1
			if vy-3 > 0:
				board[vx][vy-3] = "F"
	else:
		printo()

	if vx+2 <imgx:
		if direction ==3:
			count+=1
			board[vx+2][vy] = " "
			for i in range(-1,2,2):
				if vx+i > 0:
					board[vx+2][vy+i] = "F"
			right = 1
			board[vx+3][vy] = "F"
	else:
		printo()

	if vx-2 > 0:
		if direction ==4:
			count+=1
			left = 1
			board[vx-2][vy] = " "
			for i in range(-1,2,2):
				if vx+i > 0:
					board[vx-2][vy+i] = "F"
			if vx-3 > 0:
				board[vx-3][vy] = "F"
	else:
		printo()
	for i in range (1,len(board)):
		for j in range(1,len(board[0])):
			print(board[i][j],end=" ")
		print("")
	print('-'*20)
	check(vx,vy)

# this was the code that erased the free gap between two occupied spots
def check(vx,vy):#x,y):
	global up
	global down
	global left
	global right
	for i in range(imgx*imgx):
		direction = random.randint(0,4)
		if direction == 4:
			if vx-2>0 and board[vx-2][vy] == " ":
				board[vx-1][vy] = " "
				if vx+2<0 and board[vx+2][vy] == " ":
					board[vx+1][vy]
				if vx-2 < 0:
					break
			else:
				printo()
		elif direction == 3:
			if vx+2<imgx and board[vx+2][vy] == " ":
				board[vx+1][vy] = " "
				if vx-2>0 and board[vx-2][vy] == " ":
					board[vx-1][vy] = " "
				if vx+2 > imgx:
					break
			else:
				printo()
		elif direction == 1:
			if vy+2<imgy and board[vx][vy+2] == " ":
				board[vx][vy+1] = " "
				if board[vx][vy-2] and vy-2>0 == " ":
					board[vx][vy-1] = " "
				if vy+2 > imgy:
					break
			else:
				printo()
		elif direction == 2:
			if vy-2>0 and board[vx][vy-2] == " ":
				board[vx][vy+1] = " "
				if vy-2 < 0:
					break
			else:
				printo()
	#print("check works")
	printo()
	stopfunc()

def printo():
	print("loading")

#this is the start and the timer function was inspired by many sources online
#some of the inspirations will be posted in the comment section of seesaw
start = input("Welcome to the maze! This isn't like your regular maze, there are multiple entrances and multiples exits\nnavigate your way through, if you chose a bad entrance...too bad!\nyou have seven seconds to solve the maze, press y to start\n\n>>")
if start == "y":


	print(vx,vy)
	blank(vx,vy)
	for i in range (1,len(board)):
			for j in range(1,len(board[0])):
				print(board[i][j],end=" ")
			print("")

timeloop = True
timeloop = start
while timeloop:
	Sec+=1
	time.sleep(1)	
	if Sec >= 7:
		print("your seven seconds are up")
		quit()
else:
	print("ok no game for you")

