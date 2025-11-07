import os

import polars as pl

def generate_file_path(path: str) -> str:
    return os.path.join(os.path.dirname(__file__), path)

def main():
    csv_path = generate_file_path("data/citibike/202403-citibike-tripdata_1.csv")

    trips_df = pl.read_csv(
        source=csv_path,
        try_parse_dates=True,
        schema_overrides={
            "start_station_id": pl.String,
            "end_station_id": pl.String
        },
    ).sort(
        by="started_at"
    )

    json_path = generate_file_path("data/citibike/custom-nyc-data.geojson")
    neighbourhoods_df = (
        pl.read_json(json_path)
        .select("features")
        .explode("features")
        .unnest("features")
        .unnest("properties")
        .select("neighborhood", "borough", "geometry")
        .unnest("geometry")
        .with_columns(polygon=pl.col("coordinates").list.first())
        .select("neighborhood", "borough", "polygon")
        .filter(pl.col("borough") != "Staten Island")
        .sort("neighborhood")
    )

    neighbourhoods_coord_df = (
        neighbourhoods_df.with_row_index("id")
        .explode("polygon")
        .with_columns(
            lon=pl.col("polygon").list.first(),
            lat=pl.col("polygon").list.last(),
        )
        .drop("polygon")
    )

    stations_df = (
        trips_df.group_by(station=pl.col("start_station_name"))
        .agg(
            lon=pl.col("start_lng").median(),
            lat=pl.col("start_lat").median(),
        )
        .sort("station")
        .drop_nulls()
    )
    return trips_df 

if __name__ == "__main__":
    main()