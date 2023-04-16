import distancegetter
import csv_parser
import random

origin = input("Enter Start Destination: ")
destination = input("Enter End Destination: ")
api_key = 'AIzaSyDc6_OK5NMUMTiK3r-WsOkTzuImskrCSRc'
distance = distancegetter.get_distance(origin, destination, api_key)
car_makes = csv_parser.get_field_values('make')
car_models = csv_parser.get_field_values('model')
car_years = csv_parser.get_field_values('year')
car_emissions = csv_parser.get_field_values('co2TailpipeGpm')

print("example:", csv_parser.get_car_details(car_makes, car_models, car_years, car_emissions, random.randint(0, len(car_makes) - 1))) # for reference
make = input("Car's Make: ")
model = input("Car's model: ")
year = input("Car's year: ")

index = csv_parser.get_index(make, model, year, car_makes, car_models, car_years)
car_details = csv_parser.get_car_details(car_makes, car_models, car_years, car_emissions, index)

print(car_details[1] + " " + str(car_details[2]) + "'s carbon emissions are " + str(car_details[3]) + " g/mi")
int_distance = distance.split(' ')
gramsemissions=float(car_details[3]) * int(int_distance[0])
kgemissions=round(gramsemissions/1000, 2)
print("Total carbon emissions: " + str(kgemissions) + " kilograms")