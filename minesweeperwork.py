#Kyn Toh
#Minesweeper project with extension
#sources from ms.Healey gihub for end code minesweeper board
#and python cheat sheet
# and python library
#on my honor

import sys
import random

#user inputs
w = int(sys.argv[1])
h = int(sys.argv[2])
b = int(sys.argv[3])

#corrected version of grid
def boards():
	global board
	global board2
	board = [[0]*(w+2) for x in range(h+2)]

	#making bombs
	for i in range(b):
		global bx
		global by
		bx = random.randint(0+1, w-1)
		by = random.randint(0+1, h-1)
		board[by][bx] = "*"
		#printing +1 next to bombs so the digits display, scanning the area
		if board[by+1][bx+1]!= "*": 
			board[by+1][bx+1]+=1
		if board[by-1][bx-1] != "*":
			board[by-1][bx-1]+=1
		if board[by+1][bx-1] != "*":	
			board[by+1][bx-1]+=1
		if board[by-1][bx+1] != "*":
			board[by-1][bx+1]+=1
		if board[by][bx+1] != "*":
			board[by][bx+1]+=1
		if board[by][bx-1] != "*":
			board[by][bx-1]+=1
		if board[by+1][bx] != "*":
			board[by+1][bx]+=1
		if board[by-1][bx] != "*":
			board[by-1][bx]+=1
		else:
			#applying the data and actually changing list elements
			board[by+1][bx+1]+=1
			board[by-1][bx-1]+=1
			board[by+1][bx-1]+=1
			board[by-1][bx+1]+=1
			board[by][bx+1]+=1
			board[by][bx-1]+=1
			board[by+1][bx]+=1
			board[by-1][bx]+=1


	#end code from ms.Healey
	#reference (cheat code you can comment it out if you want)
	for i in range (1,len(board)-1):
		for j in range(1,len(board[0])-1):
			print(board[i][j],end=" ")
		print("")
	print('-'*20)

		#added borders
	board2 = [["X"]*(w+2) for z in range(h+2)]
	for i in range (1,len(board2)-1):
		for j in range(1,len(board2[0])-1):
			print(board2[i][j],end=" ")
		print("")

	start()

#failed attemps
#print("T "*(int(sys.argv[1])+2))
#for i in range (1,len(board2)-1):
#	print("T",end=' ')
#	for j in range(1,len(board2[0])-1):
#		print(board2[i][j],end=" ")
#	print("T")
#print("T "*(int(sys.argv[1])+2))
#print('-'*20)

#board2 = [["X"]*(w+2) for z in range(h+2)]
#for z in board2:
	#for i in range(h):
	#	board2 = ["-"]*h
	#for j in range(w)
	#	board2[w] = "-"
	#for k in range(h-1):
	#	board2[h] = "-"
	#for h in range(w-1)
	#	board2[w] = "-"
	#print(*z,'ttt')


def start():
	global count
	count = 0
	global xcoords
	global ycoords
	if count == b:
		win()
	else:
		xcoords = int(input("choose where(X)\n\n>>"))
		ycoords = int(input("choose where(Y)\n\n>>"))
		CF = input("clear or flag (C/F)?\n\n>>")
		#if user chooses to clear
		if CF == "C":
				if board[ycoords][xcoords] == "*":
					gameover()
				elif board[ycoords][xcoords] == 0: 
					start_check()
					#printing the recursion loop
					for i in range (1,len(board2)-1):
						for j in range(1,len(board2[0])-1):
							print(board2[i][j],end=" ")
						print("")
					start()
					if count == b:
						win()
				else:
					board2[ycoords][xcoords] = board[ycoords][xcoords]
					for i in range (1,len(board2)-1):
						for j in range(1,len(board2[0])-1):
							print(board2[i][j],end=" ")
						print("")
						

					start()
				#if user chooses to flag
		elif CF == "F":
			board2[ycoords][xcoords] = "F"
			if board[ycoords][xcoords] == "*":
				count+=1
				if count == b:
					win()
			#showing your vistory board so you can screenshot it and show it to your friends
			for i in range (1,len(board2)-1):
				for j in range(1,len(board2[0])-1):
					print(board2[i][j],end=" ")
				print("")
			start()
		else:
			print("no")
			start()

#recursion for zeros
def zerocheck(x,y):
	if board[y][x] == 0 and board2[y][x] == "X":
		board2[y][x] = 0 
		#print(x,y)
		if x<w and board2[y][x+1] == "X":			
			zerocheck(x+1,y)

		if y<h and board2[y+1][x] == "X":
			zerocheck(x,y+1)

		if x>0 and board2[y][x-1] == "X":
			zerocheck(x-1,y)

		if y>0 and board2[y-1][x] == "X":
			zerocheck(x,y-1)


#to activate the recursion and scan the area
def start_check():
	for w in range(h):
		for xcoords in range(-1,2):
			for ycoords in range(-1,2):
				zerocheck(ycoords,xcoords)

# if you lose
def gameover():
	print("gameover")
	choicea = input("do you want to restart?\n\n1 for yes\n2 for no\n\n>>")
	if choicea == "1":
		boards()
	if choicea == "2":
		quit()
	else:
		print("try again")
		gameover()

#winner winner chicken dinner!
def win():
	print("you win, goodjob")
	restart = input("do you want to play again?\n\n1 for yes\n2 for no\n\n>>")
	if restart == "1":
		boards()
	if restart == "2":
		quit()


boards()





