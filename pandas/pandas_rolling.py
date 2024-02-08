import numpy as np
import pandas as pd

def add_month_variables(sl_frame: pd.DataFrame) -> pd.DataFrame:
    """Sales/stock ratio in the past month: calculate the mean number of sales in the past month, and the mean stock level.

    Mean: mu of the stock level over the past month.
    """
    sl_frame["MEAN_STOCK_MONTH"] = np.maximum(
        0,
        sl_frame.groupby(
            ["BU_NUM", "LINE_NUM"], group_keys=False
        ).LINE_STOCK_CASES_YESTERDAY.apply(lambda x: x.rolling(window=30).mean()),
    )
#    sl_frame["MEAN_SALES_MONTH"] = np.maximum(
#        0,
#        sl_frame.groupby(
#            ["BU_NUM", "LINE_NUM"], group_keys=False
#        ).LINE_SALES_CASES_YESTERDAY.apply(lambda x: x.rolling(window=30).mean()),
#    )
#    sl_frame["SALES_STOCK_RATIO_MONTH"] = np.minimum(
#        sl_frame.MEAN_SALES_MONTH / np.maximum(sl_frame.MEAN_STOCK_MONTH, 0.0001), 1
#    )
#
    return sl_frame.groupby(
            ["BU_NUM", "LINE_NUM"], group_keys=False
        ).LINE_STOCK_CASES_YESTERDAY.apply(lambda x: x.rolling(window=30).mean())

input_data = pd.DataFrame(
        {
            "BU_NUM": [1] * 30,
            "LINE_NUM": [1] * 30,
            "LINE_STOCK_CASES_YESTERDAY": [25.0] * 30,
            "LINE_SALES_CASES_YESTERDAY": [1] * 30,
        }
        )
print(add_month_variables(input_data))
