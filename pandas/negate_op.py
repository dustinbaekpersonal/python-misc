import pandas as pd


df = pd.DataFrame({"a":[1,2,1,], "b":[4,5,4], "c": [10,20,30]})

print(df[~df["b"].isin([4])])
print(df.groupby(["a","b"]).sum())
print(df)