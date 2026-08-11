print("Movie Ticket Checker")
age = int(input("Enter Your Age:"))

if age >=18:
	has_id= input("Do you have an ID?yes/no").lower()
	if has_id =="yes":
		
		print("You can watch R-rated Movie")
	else :
		print("acces denied")
	

elif age <18 and age >=13:
	print("You can only  watch PG-13 movies")
else:
	print("Go to Kids Section")