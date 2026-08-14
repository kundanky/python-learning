#login attempt tracker
print("Login attempt tracker")
username =""
password =""
attempt = 0
total = 3
name = "sakshi"
while attempt <3:
	username = input("Enter Username:").lower()
	password = input("Enter password").lower()
	attempt = attempt +1
	total= 3-attempt
	if username == "kundanky" and  password =="ky":
		print("login successful")
		text = input("Tell us something about yourself").lower()
		words =text.split()
		words2=text.replace(" ","_")
		print(len(words))
		print(words2)
		break
	elif attempt == 3:
		print("You're locked")
	else:
		print("attempts left",total)
print(f"Welcome {name} You wrote {len(words)} words")
