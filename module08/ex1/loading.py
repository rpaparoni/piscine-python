import sys
import importlib.metadata
from typing import Any


try:
    import requests # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore


    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    

    packages_info = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }
    for pkg, msg in packages_info.items():
        version = importlib.metadata.version(pkg)
        print(f"[OK] {pkg} ({version}) - {msg}")

except (ImportError, importlib.metadata.PackageNotFoundError):
    print("Error: Missing dependencies.")
    print("To install with pip, run:")
    print("pip install -r requirements.txt")
    print("\nTo install with Poetry, run:")
    print("poetry install")
    print("poetry run python loading.py")
    sys.exit(1)


def analyze_and_plot() -> None:


    print("\nAnalyzing Matrix data...")
    df = fetch_venezuela_earthquakes()

    if df.empty:
        print("Error: No data found in the Matrix.")
        sys.exit(1)

    print(f"Processing {len(df)} data points...")

    magnitudes = df["magnitude"].to_numpy()
    depths = df["depth"].to_numpy()

    point_sizes = np.power(10, (1.5 * magnitudes - 4.0))

    print("Generating visualization...")

    plt.figure(figsize=(10, 6))
    plt.scatter(
        depths,
        magnitudes,
        s=point_sizes,
        alpha=0.5,
        c=magnitudes,
        cmap="viridis"
    )

    plt.title("Earthquake Magnitudes vs Depth in Venezuela (Since 2001)")
    plt.xlabel("Depth (km)")
    plt.ylabel("Magnitude")
    plt.colorbar(label="Magnitude")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.savefig("analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: analysis.png")


def fetch_venezuela_earthquakes() -> pd.DataFrame:

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    params: dict[str, str | float] = {
        "format": "geojson",
        "starttime": "2001-01-01",
        "minlatitude": 0.5,
        "maxlatitude": 12.5,
        "minlongitude": -73.5,
        "maxlongitude": -59.5,
        "minmagnitude": 3.0
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data: dict[str, Any] = response.json()
    features: list[dict[str, Any]] = data.get("features", [])

    parsed_data: list[dict[str, float]] = []
    for feature in features:
        properties = feature.get("properties", {})
        geometry = feature.get("geometry", {})

        mag = properties.get("mag")
        coords = geometry.get("coordinates", [0.0, 0.0, 0.0])

        if mag is not None and len(coords) >= 3:
            parsed_data.append({
                "magnitude": float(mag),
                "depth": float(coords[2])
            })
    return pd.DataFrame(parsed_data)


if __name__ == "__main__":
    analyze_and_plot()
