from flask import Flask, render_template, request
import distancegetter
import csv_parser
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    origin = request.form['origin']
    destination = request.form['destination']
    api_key = 'AIzaSyDc6_OK5NMUMTiK3r-WsOkTzuImskrCSRc'
    distance = distancegetter.get_distance(origin, destination, api_key)
    car_makes = csv_parser.get_field_values('make')
    car_models = csv_parser.get_field_values('model')
    car_years = csv_parser.get_field_values('year')
    car_emissions = csv_parser.get_field_values('co2TailpipeGpm')

    make = request.form['make']
    model = request.form['model']
    year = request.form['year']

    index = csv_parser.get_index(make, model, year, car_makes, car_models, car_years)
    car_details = csv_parser.get_car_details(car_makes, car_models, car_years, car_emissions, index)

    int_distance = distance.split(' ')
    gramsemissions=float(car_details[3]) * int(int_distance[0])
    kgemissions=round(gramsemissions/1000, 2)

    return render_template('results.html', car_make=car_details[1], car_model=car_details[2], car_year=car_details[3], distance=int_distance[0], emissions=kgemissions)

if __name__ == '__main__':
    app.run(debug=True)
