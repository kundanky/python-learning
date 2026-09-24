print("Security Check")
age = int(input("Enter Your Age"))
if age >=18 :
	has_id =input("Do you have an idcard?yes/no")
	if has_id== "yes":
		print("Entry Allowed")
	else :
		print("Entry Denied")
else :
	print("You are underage")