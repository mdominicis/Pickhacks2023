import csv
import numpy as np

def get_field_values(fieldname):
    values = []
    with open('vehicles.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            values.append(row[fieldname])
    return np.array(values)

def get_car_details(index):

    car_details = []

    #car makes
    car_makes = get_field_values('make')
    car_details.append(car_makes[index])

    #car models
    car_models = get_field_values('model')
    car_details.append(car_models[index])

    #car year
    car_years = get_field_values('year')
    car_details.append(car_years[index])

    car_emissions = get_field_values('co2TailpipeGpm')
    car_details.append(car_emissions[index])
    
    return car_details


if __name__ == '__main__':
    # only runs if this file is run
    car = get_car_details(0)
    print(car)