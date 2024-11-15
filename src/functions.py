import requests

#%% Station name from ID

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


#%% Buy and sell orders per item

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
    


#%% Next function
