import sys

# La caja fuerte: intentamos importar todo
try:
    import requests
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

# Si falla CUALQUIERA de los de arriba, Python salta aquí en vez de explotar
except ImportError:
    print("Error: Missing dependencies.")
    print("To install with pip, run:")
    print("pip install -r requirements.txt")
    print("\nTo install with Poetry, run:")
    print("poetry install")
    print("poetry run python loading.py")
    sys.exit(1)


def fetch_venezuela_earthquakes() -> pd.DataFrame:
    """Fetches earthquake data for Venezuela using the USGS API."""
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    # Coordenadas aproximadas para cubrir Venezuela
    params: dict[str, str | float] = {
        "format": "geojson",
        "starttime": "2023-01-01",
        "minlatitude": 0.5,
        "maxlatitude": 12.5,
        "minlongitude": -73.5,
        "maxlongitude": -59.5,
        "minmagnitude": 3.0  # Solo temblores de magnitud 3 o superior
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data: dict[str, Any] = response.json()
    features: list[dict[str, Any]] = data.get("features", [])

    # Extraemos solo lo que nos interesa
    parsed_data: list[dict[str, float]] = []
    for feature in features:
        properties = feature.get("properties", {})
        geometry = feature.get("geometry", {})

        mag = properties.get("mag")
        coords = geometry.get("coordinates", [0.0, 0.0, 0.0])

        # coords[2] suele ser la profundidad en la API del USGS
        if mag is not None and len(coords) >= 3:
            parsed_data.append({
                "magnitude": float(mag),
                "depth": float(coords[2])
            })

    # Pandas hace su magia y lo convierte en una tabla
    return pd.DataFrame(parsed_data)


def analyze_and_plot() -> None:
    """Analyzes data with numpy and generates matrix_analysis.png."""
    print("Analyzing Matrix data...")
    df = fetch_venezuela_earthquakes()

    if df.empty:
        print("Error: No data found in the Matrix.")
        sys.exit(1)

    print(f"Processing {len(df)} data points...")

    # Obligatorio: Usamos numpy para los cálculos matemáticos
    magnitudes = df["magnitude"].to_numpy()
    depths = df["depth"].to_numpy()

    # Calculamos el tamaño visual de los puntos usando numpy
    # (Hacemos que crezcan exponencialmente según su magnitud)
    point_sizes = np.power(10, (1.5 * magnitudes - 4.0))

    print("Generating visualization...")

    # Matplotlib dibuja el gráfico
    plt.figure(figsize=(10, 6))
    plt.scatter(
        depths,
        magnitudes,
        s=point_sizes,
        alpha=0.5,
        c=magnitudes,
        cmap="viridis"
    )

    plt.title("Earthquake Magnitudes vs Depth in Venezuela (Since 2023)")
    plt.xlabel("Depth (km)")
    plt.ylabel("Magnitude")
    plt.colorbar(label="Magnitude")
    plt.grid(True, linestyle="--", alpha=0.7)

    # Guardamos el archivo exacto que nos pide el subject
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    # Aquí iría primero tu lógica de importlib comprobando dependencias...
    # Y si todo está [OK], llamas a la función:
    analyze_and_plot()
