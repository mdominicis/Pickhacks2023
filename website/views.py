# views.py
from flask import render_template, request
from . import app
import distancegetter
import csv_parser

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    origin = request.form['origin']
    destination = request.form['destination']
    make = request.form['make']
    model = request.form['model']
    year = request.form['year']

    api_key = 'YOUR_GOOGLE_MAPS_API_KEY'
    distance = distancegetter.get_distance(origin, destination, api_key)

    car_makes = csv_parser.get_field_values('make')
    car_models = csv_parser.get_field_values('model')
    car_years = csv_parser.get_field_values('year')
    car_emissions = csv_parser.get_field_values('co2TailpipeGpm')

    index = csv_parser.get_index(make, model, year, car_makes, car_models, car_years)
    car_details = csv_parser.get_car_details(car_makes, car_models, car_years, car_emissions, index)

    int_distance = int(distance.split(' ')[0])
    gramsemissions = float(car_details[3]) * int_distance
    kgemissions = round(gramsemissions / 1000, 2)

    return render_template('results.html', car_make=make, car_model=model, car_year=year, distance=distance, emissions=kgemissions)
