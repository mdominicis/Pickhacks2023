import requests

def get_distance(origin, destination, api_key):
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + origin + '&destinations=' + destination + '&key=' + api_key
    response = requests.get(url)
    data = response.json()
    distance = data['rows'][0]['elements'][0]['distance']['text']
    return distance