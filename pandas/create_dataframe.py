import time
from datetime import datetime

import pandas as pd

branch_list = [num for num in range(100)]

model_run_id = int(time.time())
run_timestamp = datetime.utcnow().strftime(format="%Y-%m-%d %H:%M:%S")

logging_df = pd.DataFrame(
    {
        "MODEL_RUN_ID": [model_run_id]*len(branch_list),
        "RUN_TS": [run_timestamp]*len(branch_list),
        "BRANCH": branch_list,      
    }
)
print(logging_df)

logging_df["asdf"] = model_run_id + 100000000
print(logging_df)
