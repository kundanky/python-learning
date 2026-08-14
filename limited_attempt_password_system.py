print("password system")
password =""
attempts = 0
while password !="1234" and attempts <3:
	password = input("Enter Your Password:")
	attempts = attempts +1
	if password  =="1234":
		print("successful")
	elif attempts == 3:
		print("You're Locked out")
		
	else :
		print ("try again")
