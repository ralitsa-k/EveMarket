import polars as pl
import bz2
import os
from os.path import exists as file_exists
from os.path import isfile, join
import glob
import re 
import mysql.connector

from sqlalchemy import create_engine
import polars as pl
import pandas as pd

# Create a database connection (example for PostgreSQL)
# Replace the connection string with your actual database connection details
engine = create_engine('mysql://rkostova:ra77fg28@localhost:3306/eve_db')
# SQL query
query1 = 'SELECT * FROM type_category'
# Load query result into a Pandas DataFrame
types_df_pandas = pd.read_sql(query1, engine)
# Convert the Pandas DataFrame to a Polars DataFrame
types_df = pl.from_pandas(types_df_pandas)
types_df.group_by('groupID').len()



connection = mysql.connector.connect(
    host="localhost",      # e.g., 'localhost'
    user="rkostova ",        # e.g., 'root'
    password="ra77fg28",    # Your MySQL password
    database="eve_db"     # The database you want to connect to
)

query1 = 'select * from invTypes'
types_df = pl.read_da(connection.execute(query1).fetchall())

date_f = os.listdir('c:\\Users\\Ralitsa\\Documents\\All Files\\DataSci\\EveOnline/eve_data')
# grab all compressed file paths
onlyfiles = glob.glob(f'eve_data/{date_f[0]}/*.bz2')
# if csv file exists, don't overwrite it
# read the compressed file and write as csv
for file in onlyfiles:
    if not file_exists(file[:-4]):
        with bz2.BZ2File(filepath, 'rb') as zipfile:
            data = zipfile.read()  # Decompress the data
            # Convert decompressed bytes into a dataframe using Polars
            open(file[:-4], 'wb').write(data)
        
# get sell orders only 
all_data = []
# read all csv files and combined them into one, first filtering and selecting relevant columns
for files in glob.glob('eve_data/2024-08-13/*.csv'):
    df = ( pl.scan_csv(files)
                     .filter(pl.col('is_buy_order') == 'true')
                     .select('issued', 'region_id', 'price', 'type_id'))
    # add date and time of the transactions
    df2 = df.collect().with_columns(pl.lit(
        re.sub('_','T',re.search(re.escape('orders-2024')+f'.{{0,{15}}}',files).group(0)[7:])).alias('date_t'))
    all_data.append(df2)
# combine the data
day_data = pl.concat(all_data)
day_data.write_csv(f'buy_orders/market-orders-{date_f[0]}.csv')

#%% ETL

day_data.write_database('eve_data/{date_f[0]}/market-orders-{date_f[0]}', 
                        'mysql+mysqlconnector://rkostova:ra77fg28@127.0.0.1:3306/eve_db')

# string to date and string to time
day_data = day_data.with_columns(pl.col("date_t").str.to_datetime("%Y-%m-%dT%H-%M-%S"))
day_data = day_data.with_columns(Hour=pl.col('date_t').dt.hour())



#%%  check if the data is fine 
days = day_data.group_by('region_id').len()

# get type id as a category 



import matplotlib.pyplot as plt
plt.bar(days['region_id'], days['len'])