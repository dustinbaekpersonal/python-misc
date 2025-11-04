import requests
from pprint import pprint

import pandas as pd

# url = "https://api.exchangerate-api.com/v4/latest/USD"
# data = requests.get(url, verify=False)
# raw_data = data.json()
# pprint(raw_data)

# df = pd.DataFrame(raw_data)
# df.drop(["WARNING_UPGRADE_TO_V6"], axis=1, inplace=True)
# print(df)
# print(df.columns)
# print(df.index)

json_data = [
        {'stock_level': 10, 'store_id': 1, 'id': 1, 'product_name': 'milk'}, 
        {'stock_level': 10, 'store_id': 1, 'id': 2, 'product_name': 'bread'}
    ]
df = pd.DataFrame(json_data)
print(df)