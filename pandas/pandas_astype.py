import random
import time

import pandas as pd

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{end - start:.3f}")
        return result
    return wrapper

@timer
def change_astype(df):
    df = df.astype({
        "A": "string",
        "B": "string",
        })
    return df

@timer
def change_apply(df):
    df["A"] = df["A"].apply(str)
    df["B"] = df["B"].apply(str)
    return df


if __name__ == "__main__":
    num = 100_000
    long_list_float = [random.random() for _ in range(num)]
    long_list_int = [random.randint(0,10) for _ in range(num)]
    df = pd.DataFrame({
         "A":long_list_float,
         "B":long_list_int,
    })
    df=df.astype({col:"float16" for col in df.columns})
    print(df.dtypes)
    asdf = [1,2,3] 
    if asdf:
        print('asdf')
    else:
        print('asdfasdf')
    #for _ in range(10):
    #    df_astype = change_astype(df)
    #    df_apply = change_apply(df)

    #    print(df_astype.dtypes)
    #    print(df_apply.dtypes)
