import requests

def get_distance(origin, destination, api_key):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + origin + '&destinations=' + destination + '&key=' + api_key
    response = requests.get(url)
    data = response.json()
    distance = data['rows'][0]['elements'][0]['distance']['text']
    return distance

origin = input("Enter Start Destination: ")
destination = input("Enter End Destination: ")
api_key = 'AIzaSyDuQPY3dVLxfJRLshL5SwKtieHt-yaeeQA'

distance = get_distance(origin, destination, api_key)