import requests
import polars as pl

# Useless in case casual items are needed as this is already 
#   present in the csv file invTypes

# This one gets a name of an item and return the adjusted, average price and type_id

base_url = "https://esi.evetech.net/latest/"

# get type IDs from ESI
# typeids = pl.read_csv('data/invTypes.csv', columns=["typeID", "typeName"])

# col_in = input("enter type name")
# type_id = typeids.filter(pl.col("typeName")==col_in).select(pl.col("typeID")).item()

endpoint = f"markets/prices/"

# Make a GET request to the ESI API
response = requests.get(base_url + endpoint)

# Check if the request was successful
if response.status_code == 200:
    df = response.json()
    print(f"success")
    market_data = pl.DataFrame(df)
    market_data.filter(pl.col("type_id")==type_id)
    print()
else:
    print(f"Failed to fetch data: {response.status_code} - {response.text}")




