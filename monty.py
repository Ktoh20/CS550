#Kyn Toh
#Statistically there is a larger chance to win a prize if you switch because in the beginning you chose something with at 33% but now its 66% because by switching you are effectively choosing 2 choices(the crossed out one and the new one)
import random
#doors
for i in range(1001):
	board = [1,2,3]

	# while i < 1001:
	w = 0
	car = random.randint(1,3)
	choice = random.randint(1,3)
	print(car)
	print(choice)
	if car == 1:
		board.remove(1)
		board.insert(1,"car")
		board.remove(len(board)-random.randint(0,1))
		if car == choice:
			print("WON")
			# i+1
			# w+1
			print(board)
		else:
			#switch code
			choice2 = random.randint(0,1)
			if choice2==0:
				choice2 == 1
			if choice2==1:
				choice2 == 2
			if choice2 == car:
				print("won b switch")
				# i+1
				# w+1
			print(board)
	if car == 2:
		board.remove(2)
		board.insert(2,"car")
		x = random.randint(0,1)
		if x == 0:
			board.remove(len(board)-2)
		if x == 1:
			board.remove(len(board))
		if car == choice:
			print("WON")
			# i+1
			# w+1
			print(board)
		else:
			#switch code
			choice2 = random.randint(0,1)
			if choice2==0:
				choice2 == 2
			if choice2==1:
				choice2 == 1
			if choice2 == car:
				print("won b switch")
				# i+1
				# w+1
			print(board)
	if car == 3:
		board.remove(3)
		board.insert(3,"car")
		board.remove(len(board)-random.randint(1,2))
		if car == choice:
			print("WON")
			# i+1
			# w+1
			print(board)
		else:
			#switch code
			print(board)
			choice2 = random.randint(0,1)
			if choice2==0:
				choice2 == 3
			if choice2==1:
				choice2 == 1
			if choice2 == car:
				print("won b switch")
				# i+1
				# w+1

