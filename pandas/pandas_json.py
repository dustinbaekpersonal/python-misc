import pandas as pd
import requests
import json
from pprint import pprint

file = "./data/level_one.json"
with open(file, "rb") as raw_data:
    data = json.load(raw_data)
print(data)
df_children = pd.json_normalize(data, record_path=["children"], record_prefix="child_", meta=["firstName", "lastName"])
    #    .rename({0:"hobbies"}, axis=1)
print(df_children)

df_parent = pd.json_normalize(data, record_path=["hobbies"], meta=["firstName", "lastName", "age"])\
              .rename({0:"hobbies"}, axis=1)
print(df_parent)

# df_children.iloc[0,1] = 1
df_children.loc[0,"child_age"] = 2
print(df_children)
df_merged = (
    pd.merge(df_children, df_parent, how="inner", on=["firstName", "lastName"])\
        .query("child_firstName == 'Alice'")
        .loc[:, ["child_firstName", "child_age"]]
)
print(df_merged)

df_asdf = pd.merge(df_children, df_parent, how="inner", on=["firstName", "lastName"])
df_asdf = df_asdf[(df_asdf["child_firstName"] == "Alice")][["child_firstName","child_age"]]
print(df_asdf)


# json_path = "./data/another.json"
# df = pd.read_json(json_path)
# print(df)
# print(df.index)
# print(df.columns)

