import numpy as np
import pandas as pd

# # # 9. How to extract items at given positions from a series
# # # input
# # ser = pd.Series(list("abcdefghijklmnopqrstuvwxyz"))
# # pos = [0, 4, 8, 14, 20]
# # print(ser[pos])
# # print(ser.loc[pos])

# # # 10. How to stack two series vertically and horizontally ?
# # # input
# # ser1 = pd.Series(range(5))
# # ser2 = pd.Series(list("abcde"))
# # print(type(pd.concat([ser1, ser2], axis=1)))

# # # 11. How to get the positions of items of series A in another series B?
# # # input
# # ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
# # ser2 = pd.Series([1, 3, 10, 13])
# # print(ser1[ser1.isin(ser2)].index)

# # 12. How to compute difference of differences between consequtive numbers of a series?
# # input
# ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
# print(ser.diff(periods=1).tolist())
# # Desired Output
# # [nan, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 8.0]
# # [nan, nan, 1.0, 1.0, 1.0, 1.0, 0.0, 2.0]

# # 14. How to filter words that contain atleast 2 vowels from a series?
# # input
# ser = pd.Series(["Apple", "Orange", "Plan", "Python", "Money"])
# """
# Desired Output


# 0     Apple
# 1    Orange
# 4     Money
# dtype: object
# """
# from collections import Counter

# mask = ser.map(
#     lambda x: sum([Counter(x.lower()).get(i, 0) for i in list("aeiou")]) >= 2
# )
# print(ser[mask])

# 24. How to reverse the rows of a dataframe?
df = pd.DataFrame(np.arange(25).reshape(5, -1))
print(df)
print(df.iloc[::-1, :])

# df.loc[df.index[::-1], :]
