import pandas as pd

df_1 = pd.DataFrame(
        {
            "A": [1,2,3],
            "B": [1,2,3],
        }
)
df_2 = pd.DataFrame(
        {
            "A": [1,2,3],
            "B": [1,2,3],
        }
)

print(df_2.sub(df_1))
