


class Bank():
	def __init__(self,name,moneya,moneyb):
		self.name = name
		self.moneya = moneya
		self.moneyb = moneyb

	def withdraw(self, amount):
		if self.moneyb > 0:
			self.moneyb -= amount
			self.moneya += amount
			status = self.name+"just withdrew"+amount+"cash!"+self.name+"now has"+moneya+"on hand and"+moneyb+"in the bank"

		else:
			print("you don't have enought cash to withrdaw")

	def deposit(self, amount):
		if self.moneya > 0:
			self.moneya -= amount
			self.moneyb += amount
			status = self.name+"just deposit"+amount+ "of cash!"+self.name+"now has"+moneya+"on hand and"+moneyb+"in the bank"

	def close(self, amount):
		self.moneya=moneya+moneyb
		self.moneyb = 0
		status = self.name+"just closed the account"+self.name+"now has"+moneya+"on hand and no more money in the bank"
		quit()

	def stats(self):
		return "Name: "+self.name+"\nB.D.cash:" +str(self.moneyb)+"\n in hand cash:" +str(self.moneya)

name = input("what is your name\n\n>>")
imoneya = input("how much cash do you want to start with on hand?")
imoneyb = input("how much cash do you want to start in the bank?")
choice = input("what do you want to do?")
if choice == "withdraw":
	x = input("how much money do you want to withdraw")
elif choice == "deposit":
	y = input("how much money do you want to deposit")
elif choice == "close":
	close()
else:
	print("you cannot do that")





