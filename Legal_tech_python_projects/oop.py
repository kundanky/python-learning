#OOP object oriented programing
from Car import Car , ElectricCar , SportsCar
car1 = Car("BMW","M8",2025)
car2 = Car("Lamborghini","Aventador", 2016)
car1.display()
Tesla = ElectricCar("Tesla","S",2025)
Sports = SportsCar("Ferrari","F80",2025,350)
Sports.display()
Sports.speed()
print(Sports.top_speed)
print(car1.model)
print(car2.model)
Tesla.charge()
Tesla.display()