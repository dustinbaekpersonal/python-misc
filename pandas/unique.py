import pandas as pd

df = pd.DataFrame(
    {
        "foo": [1,2,3,4,4,4,1,10],
        "bar": [0]*8
    }
)

asdf = df["foo"].unique()

print(df[df["foo"].isin(asdf[:int(len(asdf)/2)])])