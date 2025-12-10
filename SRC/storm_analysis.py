import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from SRC.utils import classify_season
from SRC.plots import plot_time_series, plot_texas_map

def main():
    # Load data
    df = pd.read_csv("data/storm_events_tx.csv", low_memory=False)
    df["BEGIN_DATE_TIME"] = pd.to_datetime(df["BEGIN_DATE_TIME"], utc=True, errors="coerce")
    df = df.dropna(subset=["BEGIN_DATE_TIME"])
    df["year"] = df["BEGIN_DATE_TIME"].dt.year
    df["month"] = df["BEGIN_DATE_TIME"].dt.month

    # Classify seasons
    df["season"] = df["month"].apply(classify_season)

    # Aggregate counts
    counts = (
        df[df["season"].isin(["spring", "fall"])]
        .groupby(["year", "season"])
        .size()
        .reset_index(name="events")
    )
    pivot = counts.pivot(index="year", columns="season", values="events").fillna(0)
    pivot.to_csv("results/yearly_counts.csv")

    # Plots
    plot_time_series(pivot)
    plot_texas_map(df)

if __name__ == "__main__":
    main()