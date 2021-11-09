import pandas as pd
from os import listdir
from os.path import isfile, join

# Merge 12 months of sales data into a single CSV file
files = [f for f in listdir('./Sales_Data/') if isfile('./Sales_Data/'+f)]

all_data = pd.DataFrame()

for f in files:
    df = pd.read_csv('./Sales_Data/'+f)
    all_data = pd.concat([all_data, df])

all_data.to_csv('Merged_Data/all_data.csv', index=False)