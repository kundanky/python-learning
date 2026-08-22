#calculator
operator = input("Enter an operator (+,-,*,/:")
n1 = float(input("Enter your 1st number:"))
n2 = float(input("Enter your 2nd number:"))
if operator == "+":
	result = n1 + n2
	print(f"Your result is :{round(result,2)}")
elif operator =="-":
	result = n1 - n2
	print(f"Your result is :{round(result,2)}")
elif operator =="*":
	result = n1 * n2
	print(f"Your result is :{round(result,2)}")
elif operator =="/":
	result = n1 / n2
	print(f"Your result is :{round(result,2)}")
else :
	print(f"You entered {operator} is invalid")
degree = int(input("Enter Current temp:"))
temp = "COLD" if degree <= 10 else "HOT"
print(temp)

username = input("Enter Your 12 digit username:")
if len(username)>12:
	print("Your username can't be greater than 12 characters")
elif username.find(" ") != -1:
	print("Your username can't contain spaces")
elif not username.isalpha():
	print("Your username can't contain numbers")
else:
	print(f"Welcome!{username}(:")

