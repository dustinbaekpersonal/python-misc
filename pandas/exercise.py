import numpy as np
import pandas as pd

# # 1. How to create a series from a list, numpy array and dict?
# a_list = list("asdf")
# numpy_array = np.arange(1, 10)
# dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 5}

# # series = pd.Series(a_list)
# # series = pd.Series(numpy_array)
# series = pd.Series(dictionary)
# print(series)

# # 2. How to combine many series to form a dataframe?

# series_1 = pd.Series(list("asdf"))
# series_2 = pd.Series(list("poiu"))
# series_3 = pd.Series(list("qwer"))

# # df = pd.DataFrame({"col1": series_1, "col2": series_2})
# df = pd.concat([series_1, series_2, series_3], axis=1)
# df.columns = ["col1", "col2", "col3"]
# print(df)

# 3. How to get the items of series A not present in series B?
series_a = pd.Series(list("abcde"))
series_b = pd.Series(list("aqwer"))

print(series_a[~series_a.isin(series_b)])
# print(series_a.isin(series_b))

# # 4. How to get the items not common to both series A and series B?
# series_a = pd.Series([1, 2, 3, 4, 5])
# series_b = pd.Series([1, 2, 3, 9, 0])
# print(
#     pd.concat(
#         [series_a[~series_a.isin(series_b)], series_b[~series_b.isin(series_a)]],
#         axis=0,
#     ).reset_index(drop=True)
# )

# # 6. How to get frequency counts of unique items of a series?
# series = pd.Series([1, 2, 3, 4, 1, 2, 5, 6, 1, 1, 1])
# print(series.value_counts())

# 7. How to convert a numpy array to a dataframe of given shape? (L1)
ser = pd.Series(np.random.randint(1, 10, 35))
df = pd.DataFrame(ser.values.reshape(5, -1))
# print(df)

# 8. How to find the positions of numbers that are multiples of 3 from a series?
ser = pd.Series(np.random.randint(0, 10, 10))
print(ser[ser % 3 == 0])
print(ser.where(lambda x: x % 3 == 0).dropna())
