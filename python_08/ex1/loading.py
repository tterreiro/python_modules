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
    x_data = np.random.uniform(1, 10, 50)
    y_data = np.random.uniform(1, 10, 50)

    df = pd.DataFrame({"x": x_data, "y": y_data})

    plt.figure(figsize=(6, 6))
    ax = plt.gca()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(5)
    ax.spines['bottom'].set_linewidth(5)

    plt.scatter(df["x"], df["y"], color="#5a5a5a", s=40)
    plt.axhline(y=5.5, color="#fca5a5", linestyle="-", linewidth=5, alpha=0.8)

    plt.title("No Correlation", fontsize=16, fontweight="bold", y=-0.1)
    plt.xticks([])
    plt.yticks([])

    plt.savefig("matrix_analysis.png", bbox_inches='tight')
    plt.show()
    plt.close()

    print("Generating visualization...")
    print("Analysis complete! Results saved to: matrix_analysis.png")
