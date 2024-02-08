from datetime import datetime

import pandas as pd

df = pd.DataFrame({"col1":[1,2,3,1],
                   "col2":[1,2,4,1],
                   "col3":[5,6,7,8]})

df.insert(loc=0, column="asdf", value=pd.to_datetime(datetime.now().date()))

df_grouped=df.groupby(["col1","col2"])
for key, item in df_grouped:
    print(df_grouped.get_group(key))
    print(key)
    print(item)
    print("\n\n")
