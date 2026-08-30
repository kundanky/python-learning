#concession stand program
menu = {"pizza": 3.0 ,"lassi": 3.0,"pasta":2.5,"samosa":3.5, "smoothie":6.0,"coffee":7.0,"popcorn":2.0, "creamroll":1.5,"pastry":2.0}
cart=[]
total = 0
print("<-----Menu----->")
for key, value in menu.items():
	print(f"{key:10}: ${value:.02f}")
print("<--------------->")
while True:
	foods = input("Enter the food you want:(q to quit)").lower()
	if foods == "q":
		break
	elif menu.get(foods) is not None:
		cart.append(foods)
print()
print("<---Your Order--->")
for foods in cart:
	total += menu.get(foods)
	print(foods, end = " ")
print()
print(f"Your total is:${total:.2f}")