class Bank:
	def __init__(self, name, code):
		self.name=name
		self.code= code 
		self.branch = Branch()
		self.Branches = {}
		
	def addBranch(self):
		code= self.branch.Branch_Code
		city=self.branch.city
		self.Branches[code]= city
		
	def removeBranch(self):
		branch_code=input("Enter the branch code to remove: ")
		if branch_code in self.Branches:
			del self.Branches[branch_code]
		
	def getBranch(self):
		branch_code= input("Enter the branch code to get: ")
		print(self.Branches.get(branch_code))
		
	def getAllBranch(self):
		for code in self.Branches:
			print(self.Branches.get(code))
			
			
class Branch:
	def __init__(self, other= None):
		self.Branch_Code=0
		self.city=""
		self.account=other
		self.loan= other 
		
		self.loans= {}
		self.Accounts={}
		
	def setBranch(self):
		self.Branch_Code=input("Enter branch code: ")
		self.city= input("Enter the branch city: ")
		
	def addAccount(self):
		Type= input("Enter account type('savings' or 'current'): ")

		if Type == "savings":
			self.Accounts["Savings"]= self.account.Savings_Customers
		elif Type== "current":
			self.Accounts["Current"] = self.account.Current_Customers
		
	def removeAccount(self):
		Acc_no= input("Enter loan account number to remove: ")
		
		Type= input("Enter account type('savings' or 'current'): ")
		
		for Type in self.Accounts:
			for IDs in Type:
				if Acc_no in IDs:
					del IDs[Acc_no] 
					## IDs.pop(Acc_no, "Account not found!!!")
					
		print(f"{Acc_no} account of {Type} removed")
		
	def getAccount(self):
		Acc_no= input("Enter account number to get: ")
		
		Type= input("Enter account type('savings' or 'current'): ")
		
		for Type in self.Accounts:
			Type.get(Acc_no, "Account not found!!")
		
	def addLoan(self):
		Acc_no= input("Enter loan account number to be added: ")
		details= self.loan.Customers.get(Acc_no)
		if details:
			self.loans[Acc_no]= details, {
				"Amount": self.loan.Amount,
				"Type": self.loan.Type,
				"loan number": self.loan.Loan_No,
			}
		
		
	def removeLoan(self):
		Acc_no= input("Enter loan account number to remove: ")

		for numbers in self.loans:
			del numbers[Acc_no]
		
	def getLoan(self):
		Acc_no= input("Enter loan account number to be added: ")
		
		return self.loans.get(Acc_no, "Account not found!!!")
		
		
class Loan:
	def __init__(self, other):
		self.Loan_No= 0
		self.Amount=0
		self.Type=None
		self.customer= other
		self.Customers={}
		
	def setLoan(self):
		self.Loan_No= input("Enter loan number: ")
		self.Amount= input("Enter loan amount: ")
		self.Type = input("Enter loan type: ")
		
	def addCustomer(self):
		
		self.Customers[self.customer.Acc_no]={
			"Name": self.customer.name,
			"Address": self.customer.address,
			"Phone-number": self.customer.phone_number,
			"Job": self.customer.job,
		}
		
	def prepayment(self):
		amount= input("Enter prepayment amount: ")
		self.Amount= int(self.Amount) - int(amount)
		
	def getEMI(self):
		pass 
		
class Account:
	def __init__(self):
		self.Acc_no= 0
		self.Balance=0
		self.Savings_Customers={}
		self.Current_Customers={}
		
	def setAccount(self):
		self.Acc_no=input("Enter account number: ")
		self.Balance=input("Enter your account balance: ")
		
	def debitAmount(self, Amount):
		self.Balance = self.Balance - int(Amount)
		print(f"{Amount} has been debited from your account")
		
	def creditAmount(self, Amount):
		self.Balance += int(Amount)
		
	def getBalance(self):
		print(f"Your current account balance is ${self.Balance}")
		
class Savings_Account(Account):
	def __init__(self, other=None):
		super().__init__()
		
		self.Min_Balance=1500
		self.Date_of_Opening=input("Enter the date of opening: ")
		self.customer= other
		
	def addCustomer(self):
		
		self.Savings_Customers[self.customer.Acc_no]={
			"Date": self.Date_of_Opening,
			"Name": self.customer.name,
			"Address": self.customer.address,
			"Phone-number": self.customer.phone_number,
			"Job": self.customer.job,
		}
		
	def removeCustomer(self, Acc_no):
		if Acc_no in self.Savings_Customers.keys():
			del self.Savings_Customers[Acc_no]
		print(f"{Acc_no} account removed")
		
class Current_Account(Account):
	def __init__(self, other=None):
		super().__init__()
		
		self.Interest_rate=.10
		self.Date_of_Opening=""
		self.customer= other
		
	def setOpeningDate(self):
		self.Date_of_Opening= input("Enter the date of opening: ")
		
	def addCustomer(self):
		print(f"Creating a current account for {self.customer.name}")
		
		self.Current_Customers[self.customer.Acc_no]={
			"Date": self.Date_of_Opening,
			"Name": self.customer.name,
			"Address": self.customer.address,
			"Phone-number": self.customer.phone_number,
			"Job": self.customer.job,
		}
		
		
	def removeCustomer(self, Acc_no):
		if Acc_no in self.Current_Customers.keys():
			del self.Current_Customers[Acc_no]
		print(f"{Acc_no} account removed")
		
		
class Customer:
	def __init__(self):
		self.Acc_no= None
		self.name=None
		self.address=None
		self.phone_number= None
		self.job = None
		
	def createCustomer(self):
		self.Acc_no= input("Create an account number: ")
		self.name= input("Enter your name: ")
		self.address= input("Enter your home address: ")
		self.phone_number= input("Enter your phone number: ")
		self.job= input("What's your job: ")
		
if __name__=="__main__":
	
	bank= Bank("Sterling bank", 111)
	bank.branch.setBranch()
	bank.addBranch()
	bank.branch.setBranch()
	bank.addBranch()
	bank.branch.setBranch()
	bank.addBranch()
	print(bank.Branches)
	bank.getBranch()
	bank.removeBranch()
	bank.getAllBranch()




	
	
	account= Account()
	account.setAccount()
	
	
	
	cus1=Customer()
	cus1.createCustomer()

	current= Current_Account()
	current1= Current_Account(cus1)
	current1.setOpeningDate()
	current1.addCustomer()
	
	cus2=Customer()
	cus2.createCustomer()

	current2= Current_Account(cus2)
	current2.setOpeningDate()
	current2.addCustomer()
	print(current.Current_Customers)
	



	loan= Loan(cus1)
	loan.addCustomer()
	loan.setLoan()
	
	loan2= Loan(cus2)
	loan2.setLoan()
	loan2.addCustomer()
	print(loan.Customers)
	
	branch= Branch(loan)
	branch.addLoan()
	branch.addLoan()
	print(branch.loans)
	
	
	branch= Branch(account)
	branch.addAccount()
	branch.removeAccount()
	branch.getAccount()
	
	
