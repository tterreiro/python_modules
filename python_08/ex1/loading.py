#!/usr/bin/env python3
from importlib import util, metadata, import_module
import sys


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    dependencies = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }

    missing_pkgs = [tool for tool in dependencies.keys()
                     if not util.find_spec(tool)]

    for pkg_name, pkg_desc in dependencies.items():
        if pkg_name in missing_pkgs:
            print(f"[KO] {pkg_name} is missing!")

        else:
            version = metadata.version(pkg_name)
            print(f"[OK] {pkg_name} ({version}) - {pkg_desc}")

    if missing_pkgs:
        print("\nCRITICAL ERROR: Missing required programs.")
        print("To load these programs using pip:")
        print("  pip install -r requirements.txt")
        print("\nTo load these programs using Poetry:")
        print("  poetry install")
        print("  poetry run python loading.py")
        sys.exit(1)

    pd = import_module("pandas")
    np = import_module("numpy")
    plt = import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    matrix_data = np.random.randn(1000)
    df = pd.DataFrame(matrix_data, columns=["Signal_Value"])

    plt.figure(figsize=(10, 6))
    plt.hist(df["Signal_Value"], bins=40, color="green",
             edgecolor="black", alpha=0.7)
    plt.title("Matrix Signal Frequency Distribution")
    plt.xlabel("Signal Amplitude")
    plt.ylabel("Frequency")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.savefig("matrix_analysis.png")
    plt.show()
    plt.close()

    print("Generating visualization...")
    print("Analysis complete! Results saved to: matrix_analysis.png")
