import pandas as pd

# x = [1,2,3,4]
# y = [5,6,7,8]

# df1 = pd.DataFrame(
#     {
#         "x": x,
#         "y": y
#     }
# )


# df2 = df1.loc[0:1,:]

# print(df1.map(id))
# print(df2.map(id))

# print(id(df1))
# print(id(df2))


# df = df1
# df = df[df['x'].notnull()]
# # df['x'] = df['x'].astype(int).astype(str)
# df.loc[:, 'x'] = df.loc[:, 'x'].astype(int)


df = pd.DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5]}, index=['x', 'y', 'z'])
print(df)
#    a  b
# x  0  3
# y  1  4
# z  2  5

print(df.loc['x':'y']['a'])
# x    0
# y    1
# Name: a, dtype: int64


# this throws CopyWarning due to chained indexing makes it ambiguous if it's view or copy.
# if it's copy, then original df won't change.
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
# df.loc['x':'y']['a'] = 100
# print(df)

# Conclusion, 1. Never use chained indexing, 2. turn on copy-on-write
# pd.options.mode.copy_on_write = True


df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})

# without CoW, subset is treated as view (reference to original dataframe), so it will modify df.
# https://pandas.pydata.org/pandas-docs/stable/user_guide/copy_on_write.html#chained-assignment
# subset = df["foo"]
subset = df.loc[:,"foo"]

print(id(subset))
print(id(df["foo"]))

subset.iloc[0] = 100
print(df)

"""
When You Get a View
1. Slicing with iloc or loc:
    When you use iloc or loc to slice rows or columns, you typically get a view.
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})
subset = df.loc[:, "foo"]  # This is a view
subset.iloc[0] = 100
print(df)  # df['foo'][0] will be 100


2. Accessing a single column (potentially a view in older pandas versions):
    Accessing a column using df["col"] can sometimes return a view, especially in older versions of pandas. However, recent versions tend to return a copy to avoid ambiguity.
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})
col_view = df["foo"]  # Potentially a view


3. Using .loc and .iloc for indexing:
    Indexing using .loc or .iloc usually returns a view.
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})
view = df.iloc[:, 0:1]  # This is a view
"""

"""
When You Get a Copy
1. Using .copy() method:
    Explicitly calling .copy() creates a copy.
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})
subset = df.loc[:, "foo"].copy()  # This is a copy


2. Chained indexing:
    Chained indexing (like df["col"][row_indexer]) often results in a copy and triggers SettingWithCopyWarning.
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})
df["foo"][df["foo"] > 1] = 100  # Likely creates a copy and raises a warning


3. Using .loc and .iloc with slicing and other operations:
    Depending on the context, operations using .loc and .iloc might result in a copy.
df = pd.DataFrame({"foo": [1, 2, 3], "bar": [4, 5, 6]})
subset = df.loc[df["foo"] > 1, :]  # This might create a copy


Determining Whether an Operation Returns a View or Copy
To check whether you are working with a view or a copy, you can use the is_view attribute on the result of an operation, but this is not always reliable or available.
"""



"""
Best Practices

1. Use .loc and .iloc for clarity: These methods are preferred for accessing subsets of DataFrames. They make the intention clearer and reduce the risk of ambiguous behavior.
subset = df.loc[:, "foo"]


2. Avoid chained indexing: This can lead to ambiguous results and warnings. Instead, use .loc or .iloc for combined row and column operations.
df.loc[df["foo"] > 1, "foo"] = 100  # Clear and explicit


3. Use .copy() when you need a copy: If you need to ensure that you have a separate copy of the data that does not affect the original DataFrame, use the .copy() method.
subset = df.loc[:, "foo"].copy()
"""
