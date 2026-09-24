#banking system
print("🏦 Banking Program")
features = {1:"Show Balance",2:"Deposit",3:"Withdraw",4:"Exit"}
options = 1,2,3,4
balance = 0
for key, values in features.items():
	print(f"{key}:{values}")
def show_balance(balance):
	return balance
def deposit(balance):
			amount = float(input("Enter an amount to deposit:$"))
			if amount <=0:
				print("amount must be greater than 0")
				return balance
			else:
				balance = balance+ amount
				return balance
def withdraw(balance):
	amt = float(input("Enter an amount to withdraw:$"))
	if amt <=0:
		print("amount must be greater than 0")
		return balance
	elif amt > balance:
		print("Insufficient balance")
		return balance
	else:
		balance = balance - amt
		return balance
while True:
	choice = int(input("Enter Your Choice:"))
#	if choice  not in options:
#		print("enter a valid input")
	match choice:
		case 1:
			balance = show_balance(balance)
			print(f"Your Balance is ${balance}:")
		case 2:
			balance = deposit(balance)
			print(f"Your current balance is ${balance}:")
		case 3:
			balance = withdraw(balance)
			print(f"Your current balance is ${balance}:")
		case 4:
			print("Thank you for banking with us! 👋")
			break
		case _:
			print("invalid input")
		
			
#	elif choice == 1:
#		balance =show_balance(balance)
#		print(f"Your Balance is ${balance}:")
#	elif choice == 2:
#		balance = deposit(balance)
#		print(f"Your current balance is ${balance}:")
#	elif choice == 3:
#		balance = withdraw(balance)
#		print(f"Your current balance is ${balance}:")
#	else:
#		print("Thank you for banking with us! 👋")
#		break
		