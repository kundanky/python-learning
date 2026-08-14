number = int(input("Enter a number"))
total = 0
while number >= 1:
		if number % 3 == 0:
			number = number -1
			continue
		if number == 5:
			print("Reached 5,stopping early")
			break
		print(number)
		total= total + 1
		number = number -1
print("total numbers:",total)
	