import polars as pl
data = pl.DataFrame([
        pl.Series("col1", [1, 2], dtype=pl.Int64),
        pl.Series("col2", [3, 4], dtype=pl.Int64)
    ])
