import matplotlib.pyplot as plt
import geopandas as gpd

def plot_time_series(pivot):
    plt.figure(figsize=(10,5))
    plt.plot(pivot.index, pivot.get("spring", 0), label="Spring", color="blue")
    plt.plot(pivot.index, pivot.get("fall", 0), label="Fall", color="orange")
    plt.title("Texas Thunderstorm Wind Events: Spring vs Fall")
    plt.xlabel("Year")
    plt.ylabel("Event Count")
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/yearly_counts.png", dpi=150)

def plot_texas_map(df):
    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    usa = world[world.name == "United States of America"]

    gdf = gpd.GeoDataFrame(
        df[df["season"].isin(["spring", "fall"])],
        geometry=gpd.points_from_xy(df["BEGIN_LON"], df["BEGIN_LAT"]),
        crs="EPSG:4326"
    )

    fig, ax = plt.subplots(figsize=(8,8))
    usa.plot(ax=ax, color="white", edgecolor="black")
    colors = {"spring": "blue", "fall": "orange"}
    for season, group in gdf.groupby("season"):
        group.plot(ax=ax, markersize=10, color=colors[season], label=season.capitalize(), alpha=0.6)
    ax.set_title("Texas Thunderstorm Wind Events by Season")
    ax.legend()
    plt.tight_layout()
    plt.savefig("results/texas_map.png", dpi=150)