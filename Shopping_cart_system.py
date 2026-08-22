#shopping cart
print ("Shopping Cart")
snacks = []
prices = []
total = 0
while True:
	snack = input("Enter the snack you want or type q to quit:").lower()
	if snack == "q":
		break
	else:
		price = float(input(f"Enter the price of the {snack} $"))
		prices.append(price)
		snacks.append(snack)
		total = total + price
print("<------Your Item List ------>")
print(snacks, end =" ")
print()
print("Your total bill is $", total)