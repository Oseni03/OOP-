class BankAccount:
	def __init__(self, accountNumber, name, balance):
		self.accountNumber=int(accountNumber)
		self.name= name
		self.balance=int(balance)
		
	def deposit(self, amount):
		self.balance += amount
		print(f"You just deposited {amount} to your account")
		
	def withdraw(self, amount):
		balance = self.balance - amount
		self.balance = balance
		print(f"You just withdrawed {amount} from your bank account")
		
	def bankFees(self):
		fee= (5/100) * self.balance
		self.balance= self.balance - fee 
		print("5% bank fee was applied to your account")
		
	def display(self):
		print(f"Account name: {self.name.title()}\nAccount number: {self.accountNumber}\nAccount balance: {self.balance}\n")
		
		
bank= BankAccount(2051456655, "Oseni03", 1500)
bank.deposit(2000)
bank.withdraw(1500)
print(bank.balance)

bank.bankFees()
print(bank.balance)

bank.display()
# k.display()
# splay()
#  splay()
# ()
# splay()
