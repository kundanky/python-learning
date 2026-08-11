print("College Entry System")
name = input("Enter Your name").upper().strip()
print("Name:", name)
age = int(input("Enter Your Age"))
if age >=18:
	has_id = (input("Do you have an ID?yes/no")).strip().lower()
	if has_id== "yes":
		marks= int(input("Enter Your marks"))
		if marks>=40:
			print("Admission Eligible")
		else:
			print("Failed")
	else :
		print("ID Required")
else:
	print("Underage")