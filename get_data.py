import requests
import pandas as pd 
import polars as pl
from src.functions import get_buy_sell
# impoer functions
# get regions data
regions_data = get_buy_sell(params_curr)

regions_data.keys()
id_selected_data = pl.DataFrame(regions_data["11694"]['sell'])
