print("Currency Converter")
usd = float(input("Enter  US$ amount:"))
ex_rate = 95.45
inr = usd * ex_rate
print(f"${usd} in inr = ₹{inr :.2f}")