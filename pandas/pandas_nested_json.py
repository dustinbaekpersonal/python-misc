import pandas as pd


# data = [{'state': 'Florida',
#          'shortname': 'FL',
#          'info': {'governor': 'Rick Scott'},
#          'counties': [{'name': 'Dade', 'population': 12345},
#                       {'name': 'Broward', 'population': 40000},
#                       {'name': 'Palm Beach', 'population': 60000}]},
#          {'state': 'Ohio',
#           'shortname': 'OH',
#           'info': {'governor': 'John Kasich'},
#           'counties': [{'name': 'Summit', 'population': 1234},
#                        {'name': 'Cuyahoga', 'population': 1337}]}]

# df = pd.DataFrame(data)
# print(df["counties"])

# df_norm = pd.json_normalize(data, record_path='counties', meta=["state", "shortname", ["info","governor"]])
# print(df_norm)

json_path = "./data/banking.json"

df = pd.read_json(json_path)
print(df)

df = pd.json_normalize(json_path)
print(df)