#1
if str(grade) == "A" or str(grade) == "a":
	print("Good Work.")
#2
elif int(yards) > 17:
	yards*=2
#3
elif success() == True:
	print("Congratulations!")
#4
elif str(word)[1] = "f":
	print("Fun!")
#5
elif celsius == True:
	float(temp) = (float(temp)-32)/1.8
	print(temp)
#6
elif int(numItems) > 0:
	float(averageCost) = totalCost/numItems
	print(averageCost)
else:
	print("No Items.")
#7
elif float(pollution) < float(cutoff):
	print("Safe Condition")
else:
	print("Unsafe Condition")
#8
if float(score) < 60:
	str(grade) = "F"
elif float(score) < 70:
	str(grade) = "D"
elif float(score) < 80:
	str(grade) = "C"
elif float(score) < 90:
	str(grade) = "B"
elif float(score) <= 100:
	str(grade) = "A"
#9
if ord(letter)>int("0040",16) and ord(letter)<int("005B", 16):
	print("Uppercase")
elif ord(letter)>int("0061",16) and ord(letter)<int("007B",16):
	print("Lowercase")
elif ord(letter)>int("002f",16) and ord(letter)<int("003A",16):
	print("Digit")
else:
	print("Symbol")
#10
if int(neighbors) > 49:
	print("city")
elif int(neighbor) > 24:
	print("Suburbia")
elif int(neighbor) > 1:
	print("Rural")
else:
	print("Middle of Nowhere")
#11
if bool(doesSignificantWork) and bool(makesBreakthrough):
	nobelPrizeCandate = True
else:
	nobelPrizeCandidate = False
#12
if bool(variableTax):
	float(price) *= (float(taxRates) + 1)
#13
if str(word)[len(word)-2:] == "ly":
	type = 'Adverb'
	print(Type)
elif str(word)[len(word)-3:] == "ing":
	type = 'Gerund'
	print(Type)
elif str(word)[len(word)-1:] == "s":
	type = 'plural'
	print(Type)
else:
	print("error")

#14
if x%2 != 0:
	x*3+1
else:
	x/2
#15
if leapYear%4 == 0 and leapYear%100 == 0:
	leapYear = True
#16
if a-b<0:
	list.pop(b)
	if a-c<0:
		list.pop(c)
	elif a-c>0:
		list.pop(a)
elif b-a<0:
	list.pop(a)
	if b-c<0:
		list.pop(c)
	elif b-c>0:
		list.pop(b)
#17
if x%5==0 and -100<x<100:
	special = True
else:
	special = False
#18
if input == "a" or  input == "e" or input == "i" or  input == "o" or input == "u":
	x = 1
elif input == "y":
	x = -1
else:
	x = 0
#19
if str(dayOfweek) == "Saturday" or str(dayOfweek) == "saturday" or str(dayOfweek) == "Sunday" or str(dayOfweek) == "sunday":
	isWeekend = True 
#20
if str(month) == "April" or str(month) == "June" or str(month) == "September" or str(month) == "November":
	numDays = 30
elif str(month) == "January" or str(month) == "March" or str(month) == "May" or str(month) == "July" or str(month) == "October" or str(month) == "December":
	numDays = 30
else:
	numDays = 28
#21
if angle1 += angle2 += angle3 == 180:
	triangle = True
else:
	triangle = False 
#22
if units <= 50:
	cost = units*50
if units <= 150 and units > 50:
	cost = 50*50 += (units-50)*75
if units <= 250 and units > 150:
	cost = 50*50 + 100*75 + (units-150)*120
if units > 250:
	cost = 50*50 + 100*75 + 100*120 + ((units-250)*150)*1.2
#23
if str(language) == "English":
	print("Hello")
elif str(language) == "French":
	print("Bonjour")
elif str(language) == "Spanish":
	print("Hola")
else:
	print("YahYEET")
#24
#assuming we have 2 lists, one with pluralized words and one with singular words and that each number corrolates to a word
if number == 1:
	word = singularlist.pop(random.randint(0,len(singularlist-1))) 
	print(number+word)
else:
	word = pluralizedlist.pop(random.randint(0,len(pluralizedlist-1)))
	print(number+word)
#25
if input=="bacon":
	print("Why did you type bacon?")
else:
	print("I like bacon")
#26
#task 1
#if a number is divisible by 2 and a multiple of three, multiply it by 5
#task 2
#if a student recieves less than 50%, print F
#task 3
#if the time is after 8 pm print room restriction
#solution to task1
if x % 2 and x % 3:
	x*5
#solution to task2
if score < 50:
	print("fail")
#solution to task3
if time > 20.00:
	print("room restriction")


