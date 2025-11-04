import pandas as pd

ser = pd.Series([1, 2, 3, 4, 20, 21, 22])

# print(ser[ser.gt(20)].sum())
print(ser.max())
