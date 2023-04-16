import csv
import numpy as np

def get_field_values(fieldname):
    values = []
    with open('vehicles.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            values.append(row[fieldname])
    return np.array(values)

def get_car_details(car_makes, car_models, car_years, car_emissions, index):

    car_details = []

    car_details.append(car_makes[index])
    car_details.append(car_models[index])
    car_details.append(car_years[index])
    car_details.append(car_emissions[index])
    
    return np.array(car_details)

# gets index if you put a make, model and year of a car
def get_index(make, model, year, car_makes, car_models, car_years):
    
    for i in range(len(car_makes)):
        if(make == car_makes[i]) and (model == car_models[i]) and (year == car_years[i]):
            index = i
    return index


if __name__ == '__main__':
    # only runs if this file is run

    car_makes = get_field_values('make')
    car_models = get_field_values('model')
    car_years = get_field_values('year')
    car_emissions = get_field_values('co2TailpipeGpm')

    car = get_car_details(car_makes, car_models, car_years, car_emissions, 0)
    print(car)