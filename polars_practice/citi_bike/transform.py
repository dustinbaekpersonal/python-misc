import polars as pl

import extract

def main():
    trips_df, neighbourhoods_df, neighbourhoods_coord_df, stations_df = extract.main()
    trips_df = trips_df.select(
        bike_type=pl.col("rideable_type")
        .str.split("_")
        .list.get(0)
        .cast(pl.Categorical),
        rider_type=pl.col("rideable_type").cast(pl.Categorical),
        datetime_start=pl.col("started_at"),
        datetime_end=pl.col("ended_at"),
        station_start=pl.col("start_station_name"),
        station_end=pl.col("end_station_name"),
        lon_start=pl.col("start_lng"),
        lat_start=pl.col("start_lat"),
        lon_end=pl.col("end_lng"),
        lat_end=pl.col("end_lat"),
    ).with_columns(
        duration=pl.col("datetime_end") - pl.col("datetime_start")
    )

    trips_df = (
        trips_df.drop_nulls()
        .filter(
            (pl.col("datetime_start") >= pl.date(2024, 3, 1))
            & (pl.col("datetime_end") < pl.date(2024, 4, 1))
        )
        .filter(
            ~(pl.col("station_start") == pl.col("station_end"))
            & (pl.col("duration").dt.total_seconds() < 5 * 60)
        )
    )

    trips_df = trips_df.with_columns(
        distance=pl.concat_list("lon_start", "lat_start").geo.haversine_distance(
                pl.concat_list("lon_end", "lat_end")
            )
            / 1000
        ).select(
            "lon_start", "lon_end", "lat_start", "lat_end", "distance", "duration"
        )
    
    stations_df = (
        stations_df.with_columns(point=pl.concat_list("lon", "lat"))
        .join(neighbourhoods_df, how="cross")
        .with_columns(
            in_neighbourhood=pl.col("point").geo.point_in_polygon(pl.col("polygon"))
        ).filter(pl.col("in_neighbourhood"))
        .unique()
    )
    return

if __name__ == "__main__":
    main()