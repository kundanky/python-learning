class Car:
	def __init__(self,brand,model,year):
		self.brand = brand
		self.model = model
		self.year = year
	def display(self):
		print(f"The {self.brand} Car of model {self.model} was built in year {self.year}!")
class ElectricCar(Car):
	def charge(self):
		is_charging = True
		if is_charging:
			print("The Car is charging")
class SportsCar(Car):
	def __init__(self,brand, model, year,top_speed):
		super().__init__(brand,model,year)
		self.top_speed = top_speed
	def speed(self):
		print("This car is fast")
	