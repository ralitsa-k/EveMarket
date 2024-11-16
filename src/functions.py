import requests

#%% Buy and sell orders per item

# Use some type IDs to get their 
#   buy and sell data (only one buy and one sell table per item?)

class ShipOrder:
    def __init__(self, region, station_id, item_id):
        self.region = region
        self.item_id = item_id
        self.station_id = station_id

    # getting buy and sell orders for selected region and items
    # volumes, max, min, median, count
    #   returns a dictionary with item id as a key, and then buy and sell as keys
    def get_buy_sell(self):
        base_url = "https://market.fuzzwork.co.uk/aggregates/"
        params = {'region': self.region, 
                'types': self.item_id}
        response = requests.get(base_url, params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get data  {response.status_code}")
            return None
        
    def get_station_name(self):
        base_url = "https://esi.evetech.net/latest/"
        endpoint = f"universe/stations/{self.station_id}"
        # Make a GET request to the ESI API
        response = requests.get(base_url + endpoint)
        # Check if the request was successful
        if response.status_code == 200:
            stations = response.json()
            print(f"success")
        else:
            print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return stations['name']
        
