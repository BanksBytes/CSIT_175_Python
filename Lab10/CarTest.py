#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.1 Convertible class test fixture



# Import from the parent (base) class
from Convertible import Convertible
from RaceCar import Racecar

print("Convertible:")
make = input("Enter make: ")
model = input("Enter model: ")
vin = input("Enter VIN: ")
color = input("Enter color: ")
top_up_yn = input("Enter is top up? (yes/no): ")


if top_up_yn.upper() == "YES":
    is_top_up = True
else:
    is_top_up = False

# create an instance of a Convertible
my_car = Convertible(vin, make, model, color, is_top_up)


# invoke the to_string() method and display the object's contents
print(my_car.to_string())


print("\nRacecar:")
make = input("Enter make: ")
model = input("Enter model: ")
vin = input("Enter VIN: ")
color = input("Enter color: ")
horse_power = input("Enter the Horse Power: ")

# create an instance of a Racecar
my_racecar = Racecar(vin, make, model, color, horse_power)

# invoke the to_string() method and display the object's contents
print(my_racecar.to_string())