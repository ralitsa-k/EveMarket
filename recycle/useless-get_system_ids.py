import requests
import polars as pl
import unittest


# this script is meant to get station names from IDs, but it is
# unnecessary because that is already contained in 

# get station name from ID

def get_station_name(station_id):
    base_url = "https://esi.evetech.net/latest/"
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

get_station_name(60015181)

station_info = pl.read_csv('staStations.csv')

station_info_sample = station_info.sample(20)
station_info_sample.with_columns(pl.col('stationID').apply(lambda x: get_station_name(x)).alias('StationName'))
