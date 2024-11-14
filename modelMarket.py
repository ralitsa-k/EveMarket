import requests
import polars as pl
import psycopg2 as pg2
from datetime import datetime
from dateutil.relativedelta import relativedelta


region_id = 10000002  # The Forge
type_id = 34  # Tritanium

response = requests.get(f'https://esi.evetech.net/latest/markets/{region_id}/history/?datasource=tranquility&type_id={type_id}')
df = response.json()


response = requests.get(f'https://esi.evetech.net/latest/markets/{region_id}/history/')
df = response.json()


df = pl.DataFrame(df)

# change date string to date 
df = df.with_columns(pl.col("date").str.to_date("%Y-%m-%d"))

df.filter(pl.col("Year").is_between(datetime(2023,7,7), datetime(2024,7,7)))

filtered_range_df = df.filter(pl.col("date")>(datetime.now()-relativedelta(years=1)))


