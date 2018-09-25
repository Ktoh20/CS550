# Kyn Chanin Toh 
#Assignment due tuesday september 25th
#Adventure game: the Himalayas


username = input("I'm sorry but what is your name again?")
friend = input("And your friend?")

#how to start
def start():

	while True:
		try:
			choice = input("\n\n\n\n\n\n\nGreetings " +username+ "! \n\nYou have been selected on a special trip to the Himalayas with " +friend+  " to investigate the effects of climate change on the alps, now where would you like to stay? \n 1) stay with locals \n 2) or stay in the alps \n\n>>")
			if choice == "1":
				local()
				break
			elif choice == "2":
				alps()
				break
			else:
				print("Try again, enter a 1 or a 2")
		except ValueError:
			print("try again")
				

#first choice, yeti story line
def alps():
			print("Awesome! \n\n\n Three days later, you set up camp 3000 metres high. The atmosphere is thin up here, you feel the cold breeze brush through your body." +friend+ " warned you about the harsh conditions. \n as the sun's warmth dissapears behind the cold mountains, you snuggle in your sleeping bag.")
			choicea = input("But you can't get a blink of sleep! the wind constantly thrases against your tent. Suddenly, you hear a loud roar! What do you do? \n\n 1)stay inside your tent \n 2)go outside to investigate \n 3)or try to kill that thing disturbing your sleep\n\n\n>>")
			if choicea == "1":
				stay()
			elif choicea == "2":
				gout()
			elif choicea == "3":
				killa()
			else:
				print("Try again, enter a 1, 2, or 3")
				alps()



#second choice, smuggler story line
def local():
	choicek = input("as you and " +friend+ " continue research you guys hear rumours about a yeti, what do you do?\n\n1)investigate\n2)or ignore\n\n>>")
	if choicek == "1":
		investing()
	elif choicek == "2":
		ignore()
	else:
		print("hey, please print 1 or 2")
		local()

#a possible choice for the smuggler story line
def investing():
	choicel = input("the rumours came from the dissapearing goat, as you and "+friend+ " investigate, you see robbers smuggling the goats! What do you do?\n\n1)follow the smuggler\n2)or ignore it\n\n>>")
	if choicel == "1":
		smugglerz()
	elif choicel == "2":
		ignore()
	else:
		print ("ok, please enter a 1 or 2")
		investing()

#follow smuggler
def smugglerz():
	choicem = input("as you follow the smugglers through bendy roads and cliffs, you reach their hideout. However, "+friend+ " trips and makes a sound! As the smugglers approach you what do you do?\n\n1)pick up the pistol next to you and fight them\n2)or pick up the knife\n\n>>")
	if choicem == "1":
		gun()
	elif choicem == "2":
		knife()
	else:
		print("insert 1 or 2")
		smugglerz()

#ignore whats going on
def ignore():
	print("you ignore this phenomenon and complete your research, you make alot of money off your research but leave tibet in an economic crisis as they run out of goat. For the rest of your life you will have to live with the guilt of not investigating what happened with the goat.")

#if the gun is your weapon of choice
def gun():
	print("you pick up the gun and fire it! However, the kickback is too strong and you fall off a cliff shattering your skull, you are left there to die as "+friend+ " is being tortured")

#if the knife is your weapon of choice
def knife():
	print("you pick up the knife and somehow manage to stab a smuggler, " +friend+ " then takes that smugglers gun and chases off the other smugglers. You wonder why the goat was so important, so you go visit a local biology lab and find out that the milk of the mountain goats contain the cure for cancer! Furthermore, you complete your research on climate change and win a nobel prize for your findings! You become a billionaire and live the rest of your life in peace and harmony.")

#stay in tent after hearing yeti
def stay():
	print("you huddle in your sleeping bag. As your eyes shut you dream, a disturbing dream. In your dream, you hear your advisor scream and yell, but your feet are rooted the ground")
	choiceb = input("the next day you walk out and see your advisors tent ripped apart! the scent of blood lingers in the air," +friend+ " beside you starts screaming, but you notice a trail of blood\n\nwhat do you do?\n\n1)follow the blood trail\n2)or head back to the city\n\n>>")
	if choiceb == "1":
		follow()
	elif choiceb == "2":
		city()
	else:
		print("Try again, type 1, or 2 please")
		stay()


#first confrontation with yeti
def gout():
		choicec = input("you zip open your tent, and you see a YETI! \n\n what do you do? \n1)hide\n2)or stay outside\n\n\n>>")
		if choicec == "1":
			hide()
		elif choicec == "2":
			stayout()
		else:
			print("Try again, print 1 or 2 please")
			gout()


#try to kill yeti
def killa():
	print("You run out of your tent to encouter " +friend+ "'s corpse on the ground, their clothes tattered, torso ripped, and face disembled. You look up and see an overcasting shadow. It wasn't an animal, but more human like, dawn's light reflects off its silver hair. It jumps and the next thing you feel is it's hands plummaging into your body. You see your heart in it's mouth and your body starts to feel cold...")

#SOS 1
def city():
	print("You search the advisors bag and find a walkie talkie. The SOS message is received and the helicopter should arrive anytime now. As you wait you feel the temperature drop, you see the helicopter in the distance. Suddenly,a massive object collides into the helicopter rear! The helicopter loses control and dives toward you!" +friend+ "'s body is ripped in half by the propellers, you hear a familiar roar.\n\n Behind you stands the monstrosity that took your advisor. It was the yeti. You feel sharp debris slide through your body, as the yeti walks back into the mist. Your body starts to feel cold, and your blood seeps into the snow.")

#try to hunt yeti
def follow():
	choiced = input("you gather the rest of the team and hike through the tall mountains, after a long hike the trail ends at an abandoned monestary\n\n do you\n1)enter the front door\n2)or enter through the rear?\n\n>>")
	if choiced == "1":
		front()
	elif choiced == "2":
		rear()
	else:
		print("please print 1 or 2" +username)
		follow()

#try to hide from yeti
def hide():
	choicej = input("you hide behind your tent, and hear the advisor scream. You realize that you couldve prevented that, what do you do?\n\n1)call SOS\n2)or wake everybody up and follow the blood trail left behind\n\n\n>>")
	if choicej == "1":
		city()
	elif choicej == "2":
		follow()
	else:
		print("please input 1 or 2")
		hide()

#dont move, hope for the best
def stayout():
	print("the yeti spots you! It runs over and sinks its fangs into your arm. You lose all feeling in your arm.......You wake up behind bars, and the yeti is preparing a fire, you are surrounded by corpses and bones of humans, and animals. The yeti turns around and grins.")

#enter thru the front of the monestary
def front():
	choicef = input("You and"+friend+ " walk into the monestary, it's wooden walls stretch to the sky, and it still has vases, jewelry, and antiques left untouched. However, on the ground you see the corpse of your advisor!\n what do you do? \n\n1)run away\n2)or bring the corpse with you to base\n\n\n>>")
	if choicef == "1":
		runaway()
	elif choicef == "2":
		bringback()
	else:
		print(username+ " you already know the drill!")
		front()


#enter thru the rear of the monestary
def rear():
	print("you wander into the monestary, and before you stands the YETI! It slaughters your friends one by one, and " +friend+ " tries to escape but is impaled by the yetis fangs. You lose all hope and accept your inevitable death...")

#try to escape yeti
def runaway():
	print("you and" +friend+ " decide to runaway, but as you turn around you hear a roar, and then screams. Then you feel an object slide through your chest, as you look down you see a table leg sticking out your chest. You cough blood, and you start to feel sleepy...")

#try to bring back advisor corpse for a proper burial
def bringback():
	choiceg = input("as your team starts to put your advisor into a corpse bag, you guys hear a roar from inside! Your team starts to panic and hide! What do you do? \n\n1)hide behind rock\n2)or hide under a table inside the monestary?\n\n\n>>")
	if choiceg == "1":
		rock()
	elif choiceg == "2":
		dtable()
	else:
		print("please choose 1 or 2")
		bringback()

#hide under dining table
def dtable():
	print("you see a knife under the table with you, unfortunately "+friend+" impales you with the knife and leaves you as yeti bait as the crew escapes. You realize your mistakes in life, and close your eyes accepting your fate")

#hide under rock
def rock():
	choiceh = input("you slide behind a rock, and you hear heavy footsteps behind you--just to confirm--you peek over the rock and see the yeti's back turned against you\n\nwhat do you do?\n1)attack\n\n2)or keep hiding\n\n\n>>")
	if choiceh == "1":
		smash()
	elif choiceh == "2":
		keephide()
	else:
		print("...please print 1 or 2...")
		rock()

#attack the yeti
def smash():
	print("you see a boulder next to you and pick it up and slam it onto the yeti's head, this caused it's skull to rupture and you just immobilized a yeti!!! After searching the advisors pockets you use a flare gun and get back safely. You finish your research and help study the yeti's corpse with a nearby biology research lab and come up with revolutionary studies. You are awarded the nobel prize and your research on climate change earns you even more!\n\n you buy a resort and a penthouse in newyork, and as you settle into your new life you recieve a call from a professor. He wants you in the amazon...")

#dont move and hope for the best
def keephide():
	print("you keep hiding. The yeti picks off your crew one by one, and eventually you.")


start()
