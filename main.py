import sqlite3, os

os.system("clear")

# Create database and add tables
db = sqlite3.connect('Bank.db')

# Check tables
try:
	db.execute("SELECT * FROM Bank")
except:
	query_file = open('CreateQuery.sql', 'r')
	db.executescript(query_file.read())
	query_file.close()

def bank_create(code, b_name, addr, b_code, branch_code):
	"""Create a bank"""
	db.execute(f"INSERT INTO Bank( Code, Bank_Name, Addr, Bank_Code, Branch_no) VALUES ('{code}','{b_name}','{addr}','{b_code}','{branch_code}');")

def branch_create(addr, branch_no, b_code):
	"""Create branch"""
	db.execute(f"INSERT INTO Branch( Addr, Branch_no, Bank_Code) VALUES ('{addr}','{branch_no}','{b_code}');")

def bank_list():
	"""Reaturn all bank"""
	bank_tuple = list(db.execute("SELECT * FROM Bank"))
	bank_li = []
	for b in bank_tuple:
		bank_li.append({
		"Code" : b[0],
		"Bank_Name" : b[1],
		"Addrb_code" : b[2],
		"Bank_Code": b[3],
		"Branch_no": b[4]
		})
	return bank_li

def account_list():
	"""Return all account"""
	account_tuple = list(db.execute("SELECT * FROM Account"))
	account_list = []
	for a in account_tuple:
		account_list.append({
			'Acct_no' : a[0],
			'Balance' : a[1],
			'Acct_Type' : a[2],
			'Bank_Code' : a[3],
			'Branch_no' : a[4],
			"inventory" : a[5]
		})
	return account_list

def branch_list():
	"""Return all branch"""
	branches_tuple = list(db.execute("SELECT * FROM Branch"))
	branches_list = []
	for b in branches_tuple:
		branches_list.append({
		"addr" : b[0],
		"branch_no" : b[1],
		"b_code" : b[2]
		})
	return branches_list


# Account
def account_create(Acct_no, Balance, Acct_Type, Bank_Code, Branch_no):
	"""Create Account"""
	try:
		next(bank for bank in bank_list() if bank["Bank_Code"] == Bank_Code)
		next(Branch for Branch in branch_list() if Branch["branch_no"] == Branch_no)
		db.execute(f"INSERT INTO Account(Acct_no, Balance, Acct_Type, Bank_Code, Branch_no) VALUES ('{Acct_no}','{Balance}','{Acct_Type}','{Bank_Code}','{Branch_no}');")
		return print("Create Account succesfull")
	except:
		return print("Plase enter valid information")

def account_remove(account_no):
	"""Remove Account"""
	try:
		next(account for account in account_list() if account["Acct_no"] == account_no)
		db.execute(f"DELETE FROM Account WHERE Acct_no='{account_no}';")
	except:
		return print("Plase enter valid information")

def increase_funds(account_no, money):
	"""Afzayesh vajhe"""
	try:
		account = next(account for account in account_list() if account["Acct_no"] == account_no)
		db.execute(f"UPDATE Account SET inventory = {account['inventory']+money} WHERE Acct_no='{account_no}';")
	except:
		return print("Plase enter valid information")

def withdraw_money(account_no, money):
	"""Bardash vajhe"""
	try:
		account = next(account for account in account_list() if account["Acct_no"] == account_no)
		if account['inventory']-money < 0:
			print("account not have money")
		else:
			db.execute(f"UPDATE Account SET inventory = {account['inventory']-money} WHERE Acct_no='{account_no}';")
	except print(0):
		pass

def account_inventory(account_no):
	""" Inventory """
	try:
		account = next(account for account in account_list() if account["Acct_no"] == account_no)
		if account['inventory']:
			return account["inventory"]
		else:
			print("account not have money")
	except :
		pass

# /////////////////////////////////////////////////////////////////////////////////
# set default bank and branch 
bank_create(code='1',b_name='test',addr='testa-ddress',b_code='1',branch_code='1')
branch_create('1','1','1')


account_create("1", "1", "1", 1, 1)
increase_funds('1',100)

################################################################################
print('1. Account Inventory')
print('2. Create Account')
print('3. Remove Account')
print('4. Withdrow Money')
print('5. Increase Funds')
print('Q : Quit')
input_str = ''
while input_str not in ['Q','q']:
	input_str = ''
	if input_str not in ['1','2','3','4','5']:
		input_str = input('Enter number : ')
	
	
	if input_str == '1': # Account Inventory
		acc_no = input('Enter Account nomber : ')
		print('-'*50)
		print(f'{acc_no} : {str(account_inventory(acc_no))}T'.center(50))

	elif input_str == '2': # Create Account Acct_no, Balance, Acct_Type, Bank_Code:int, Branch_no:int
		try:
			Acct_no = input('Account Nomber : ')
			Balance = input('Account Balance : ')
			Acct_Type = input('Account Type : ')
			Bank_Code = int(input('Account Bank Code : '))
			Branch_no = int(input('Account Branch Nomber : '))
			account_create( Acct_no, Balance, Acct_Type, Bank_Code, Branch_no )
		except:
			print('Enter valid values')
		

	elif input_str == '3': # Remove Account
		acc_no = input('Account nomber : ')
		account_remove(acc_no)
		print('Remove Account succesfull')

	elif input_str == '4': # Withdrow Money
		try:
			acc_no = input('Account nomber : ')
			money = int(input('Money : '))
			withdraw_money( acc_no, money )
		except:
			print('Enter valid values')

	else:				   # Increase Funds
		if input_str == '5':
			try:
				acc_no = input('Account nomber : ')
				money = int(input('Money : '))
				increase_funds( acc_no, money )
			except:
				print('Enter valid values')

print('----------END----------'.center(50))


db.close()