import requests


# get station name from ID
def get_station_name(station_id):
    base_url = "https://esi.evetech.net/latest/"
    station_id = 60015181
    endpoint = f"universe/stations/{station_id}"

    # Make a GET request to the ESI API
    response = requests.get(base_url + endpoint)
    # Check if the request was successful
    if response.status_code == 200:
        stations = response.json()
        print(f"success")
    else:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
    return stations['name']


# {'34': {'buy': {'weightedAverage': '3.0881533201273763',
#    'max': '5.0',
#    'min': '0.01',
#    'stddev': '1.377445895533451',
#    'median': '4.0',
#    'volume': '3472929648.0',
#    'orderCount': '41',
#    'percentile': '4.549248341744699'},
#   'sell': {'weightedAverage': '6.220267217020354',
#    'max': '50000.0',
#    'min': '4.11',
#    'stddev': '6399.608737911598',
#    'median': '6.045',
#    'volume': '18374732618.0',
#    'orderCount': '124',
#    'percentile': '4.804705309893614'}},

# Use some type IDs to get their 
#   buy and sell data (only one buy and one sell table per item?)

params_curr = {
    'region': '10000002',
    'types': '11694,35,36,37,38,39,40'}

# getting buy and sell orders for selected region and items
# volumes, max, min, median, count
#   rreturns a dictionary with item id as a key, and then buy and sell as keys
def get_buy_sell(params):
    base_url = "https://market.fuzzwork.co.uk/aggregates/"
    response = requests.get(base_url, params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data  {response.status_code}")
        return None
    

