import pandas as pd

df = pd.DataFrame({'A' : ['foo', 'foo', 'foo', 'bar','bar', 'bar'],
                   'B' : ['one', 'one', 'two', 'three','two', 'two'],
                   'C' : [0, 0, 1, 2, 2, 2]
                   })
#
#df["C_transformed"] = df.groupby(['A','B']).C.transform(lambda x: any(x != 0))
#print(df)
grouped = df.groupby(['A'])["C"]
print(grouped.transform(lambda x: any(x != 0)))
#print(grouped.transform(lambda x: (x - x.mean()) / x.std()))
#for key, item in grouped:
#    print(item)
print(any([False, False, True]))
