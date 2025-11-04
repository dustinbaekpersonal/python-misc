import random

import pandas as pd



final_df = pd.DataFrame(
    {
        "foo": [0,0],
        "bar": [0,0]
    }
)

output_list = []
for _ in range(2):
    output_df = pd.DataFrame(
        {
            "foo": [random.randint(0, 100) for _ in range(10)],
            "bar": [random.randint(0, 100) for _ in range(10)]
        }
    )
    output_list.append(output_df)
    # print(output_list)

# output_list = output_list.append(final_df)
asdf = pd.concat(output_list, axis=0, ignore_index=True)

print(asdf)

asdf = pd.DataFrame()

if asdf is not None:
    print('asdf')