print("BMI CALCULATOR")
weight = float(input("Enter Your weight (KG):"))
height=float(input("Enter Your height (m):"))
BMI = weight / (height * height)
print(f"Your BMI is{BMI: .2f}")
if BMI <18.5:
	print("Category:Underweight")
elif 18.5 <= BMI <= 24.9:
	print("category:normal")
elif 25 <= BMI <=29.9:
	print("category:overweight")
else:
	print("category:obese")
	