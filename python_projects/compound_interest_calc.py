#Compound interest calculator
principle = 0
rate = 0
time = 0
while True:
	principle = float(input("Enter your principle amount:"))
	if principle <0:
		print("principle amount can't be less than 0")
	else:
		break
while True:
	rate = float(input("Enter the rate:"))
	if rate <0:
		print("rate  can't be less than 0")
	else:
		break
while True:
	time = int(input("Enter time in years:"))
	if time <0:
		print("time  can't be less than 0")
	else:
		break
total = principle * pow( (1 + rate / 100) ,time)
print(f"Compound Interest after {time} year/s is:${total:.2f}")

