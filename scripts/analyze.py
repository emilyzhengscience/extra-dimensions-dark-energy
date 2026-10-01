from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "Pantheon+SH0ES.dat"
FIG_DIR = ROOT / "figures"
RESULT_DIR = ROOT / "results"

FIG_DIR.mkdir(exist_ok=True)
RESULT_DIR.mkdir(exist_ok=True)

OMEGA_MIN = 0.0
OMEGA_MAX = 1.0
OMEGA_STEP = 0.001


def load_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"{DATA_FILE} does not exist.\nRun: python scripts/download_data.py"
        )

    df = pd.read_csv(DATA_FILE, sep=r"\s+")
    required = {"zHD", "m_b_corr", "IS_CALIBRATOR"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {sorted(missing)}")

    sample = df[(df["zHD"] > 0.01) & (df["IS_CALIBRATOR"] == 0)].copy()
    sample = sample[
        np.isfinite(sample["zHD"]) & np.isfinite(sample["m_b_corr"])
    ]
    return df, sample.sort_values("zHD").reset_index(drop=True)


def dimensionless_luminosity_distance(z, omega_m):
    """Flat model: Omega_Lambda = 1 - Omega_m."""
    z = np.asarray(z, dtype=float)
    omega_lambda = 1.0 - omega_m

    grid = np.linspace(0.0, float(np.max(z)), 20000)
    e_z = np.sqrt(omega_m * (1.0 + grid) ** 3 + omega_lambda)
    comoving = cumulative_trapezoid(1.0 / e_z, grid, initial=0.0)

    return (1.0 + z) * np.interp(z, grid, comoving)


def evaluate_model(z, observed_mag, omega_m):
    """Evaluate one trial universe and return its prediction and RMSE."""
    dl = dimensionless_luminosity_distance(z, omega_m)
    shape = 5.0 * np.log10(dl)

    # Fit one common vertical offset so the comparison is about curve shape.
    offset = float(np.mean(observed_mag - shape))
    prediction = shape + offset

    residual = observed_mag - prediction
    rmse = float(np.sqrt(np.mean(residual ** 2)))

    return {
        "omega_m": float(omega_m),
        "omega_lambda": float(1.0 - omega_m),
        "offset": offset,
        "prediction": prediction,
        "residual": residual,
        "rmse": rmse,
    }


def scan_parameter_space(z, observed_mag):
    """
    Test every Omega_m from 0.000 through 1.000 in steps of 0.001.
    No preferred 0.3/0.7 answer is supplied.
    """
    n_steps = int(round((OMEGA_MAX - OMEGA_MIN) / OMEGA_STEP))
    omega_values = np.linspace(OMEGA_MIN, OMEGA_MAX, n_steps + 1)

    rows = []
    for omega_m in omega_values:
        result = evaluate_model(z, observed_mag, omega_m)
        rows.append({
            "Omega_m": result["omega_m"],
            "Omega_Lambda": result["omega_lambda"],
            "RMSE_mag": result["rmse"],
        })

    scan = pd.DataFrame(rows)
    best_row = scan.loc[scan["RMSE_mag"].idxmin()]
    return scan, best_row


def binned_mean(x, y, bins):
    centers, means = [], []
    for i, (lo, hi) in enumerate(zip(bins[:-1], bins[1:])):
        mask = (x >= lo) & ((x <= hi) if i == len(bins) - 2 else (x < hi))
        if mask.sum() >= 3:
            centers.append(np.sqrt(lo * hi))
            means.append(np.mean(y[mask]))
    return np.asarray(centers), np.asarray(means)


def make_figures(sample, scan, best_model, matter_only):
    z = sample["zHD"].to_numpy(float)
    m = sample["m_b_corr"].to_numpy(float)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(z, bins=40)
    ax.set_xlabel("Hubble-diagram redshift z")
    ax.set_ylabel("Number of light-curve entries")
    ax.set_title("Figure 1 — Pantheon+ redshift distribution")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "01_redshift_distribution.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(z, m, s=8, alpha=0.28, label="Pantheon+ observations")
    ax.plot(
        z, best_model["prediction"], linewidth=2,
        label=(
            rf"Best scanned: $\Omega_m={best_model['omega_m']:.3f}$, "
            rf"$\Omega_\Lambda={best_model['omega_lambda']:.3f}$"
        ),
    )
    ax.plot(
        z, matter_only["prediction"], linewidth=2, linestyle="--",
        label=r"Matter-only endpoint: $\Omega_m=1$",
    )
    ax.set_xscale("log")
    ax.set_xlabel("Hubble-diagram redshift z")
    ax.set_ylabel(r"Corrected standardized magnitude $m_{b,\mathrm{corr}}$")
    ax.set_title("Figure 2 — Observations and discovered best model")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG_DIR / "02_hubble_diagram.png", dpi=180)
    plt.close(fig)

    bins = np.geomspace(z.min(), z.max(), 18)
    zb, rb = binned_mean(z, best_model["residual"], bins)
    zm, rm = binned_mean(z, matter_only["residual"], bins)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axhline(0.0, linewidth=1)
    ax.plot(zb, rb, marker="o", label="Best scanned model")
    ax.plot(zm, rm, marker="o", label="Matter-only endpoint")
    ax.set_xscale("log")
    ax.set_xlabel("Hubble-diagram redshift z")
    ax.set_ylabel("Mean residual = observation - prediction (mag)")
    ax.set_title("Figure 3 — Binned residuals")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG_DIR / "03_residuals.png", dpi=180)
    plt.close(fig)

    # Main result: all 1,001 tested models.
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.plot(scan["Omega_m"], scan["RMSE_mag"], linewidth=2)
    ax.scatter(
        [best_model["omega_m"]], [best_model["rmse"]],
        s=90, zorder=4, label="Minimum RMSE"
    )
    ax.scatter(
        [1.0], [matter_only["rmse"]],
        s=60, zorder=4, label="Matter-only endpoint"
    )
    ax.axvline(best_model["omega_m"], linestyle="--", linewidth=1)
    ax.annotate(
        (
            f"Minimum\n"
            f"Ωm = {best_model['omega_m']:.3f}\n"
            f"ΩΛ = {best_model['omega_lambda']:.3f}\n"
            f"RMSE = {best_model['rmse']:.4f}"
        ),
        xy=(best_model["omega_m"], best_model["rmse"]),
        xytext=(best_model["omega_m"] + 0.17, best_model["rmse"] + 0.018),
        arrowprops={"arrowstyle": "->"},
    )
    ax.set_xlabel(
        r"Trial matter density $\Omega_m$"
        "\n"
        r"(flat assumption: $\Omega_\Lambda=1-\Omega_m$)"
    )
    ax.set_ylabel("RMSE (mag) — smaller is better")
    ax.set_title(f"Figure 4 — Full parameter scan ({len(scan)} models)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIG_DIR / "04_rmse_parameter_scan.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.5, 5))
    labels = ["Matter\nΩm", "Dark-energy-like\nΩΛ"]
    values = [best_model["omega_m"], best_model["omega_lambda"]]
    bars = ax.bar(labels, values)
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2, value,
            f"{100*value:.1f}%", ha="center", va="bottom"
        )
    ax.set_ylim(0, 1)
    ax.set_ylabel("Density parameter")
    ax.set_title("Figure 5 — Components of the best scanned flat model")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "05_best_model_components.png", dpi=180)
    plt.close(fig)


def main():
    full, sample = load_data()
    z = sample["zHD"].to_numpy(float)
    observed_mag = sample["m_b_corr"].to_numpy(float)

    # First discover the minimum from the complete grid.
    scan, best_row = scan_parameter_space(z, observed_mag)
    scan.to_csv(RESULT_DIR / "omega_scan.csv", index=False)

    best_model = evaluate_model(z, observed_mag, float(best_row["Omega_m"]))

    # This is merely the Omega_m=1 endpoint of the same scan.
    matter_only = evaluate_model(z, observed_mag, 1.0)

    make_figures(sample, scan, best_model, matter_only)

    pd.DataFrame([
        {
            "result": "Best scanned model",
            "Omega_m": best_model["omega_m"],
            "Omega_Lambda": best_model["omega_lambda"],
            "RMSE_mag": best_model["rmse"],
        },
        {
            "result": "Matter-only endpoint",
            "Omega_m": 1.0,
            "Omega_Lambda": 0.0,
            "RMSE_mag": matter_only["rmse"],
        },
    ]).to_csv(RESULT_DIR / "model_comparison.csv", index=False)

    text = f"""Pantheon+ parameter-scan results
=================================

DATA
----
Rows in released table: {len(full)}
Rows in selected Hubble-flow sample: {len(sample)}
Redshift range: {z.min():.5f} to {z.max():.5f}

MODEL ASSUMPTION
----------------
Spatially flat matter + Lambda model:

    Omega_m + Omega_Lambda = 1

PARAMETER SEARCH
----------------
Omega_m range: {OMEGA_MIN:.3f} to {OMEGA_MAX:.3f}
Step size:     {OMEGA_STEP:.3f}
Models tested: {len(scan)}

The program was NOT given Omega_m = 0.3 or 0.35 as the expected answer.
Every grid value was evaluated and the smallest RMSE was selected.

BEST MODEL FOUND
----------------
Omega_m      = {best_model['omega_m']:.3f}
Omega_Lambda = {best_model['omega_lambda']:.3f}
RMSE          = {best_model['rmse']:.6f} mag

MATTER-ONLY ENDPOINT
--------------------
Omega_m      = 1.000
Omega_Lambda = 0.000
RMSE          = {matter_only['rmse']:.6f} mag

INTERPRETATION
--------------
For each trial model:

    residual = observed magnitude - predicted magnitude

RMSE summarizes the overall size of those residuals. Smaller is better.

Within this simplified model, the scan discovers the Omega values above
because they give the minimum RMSE. Matter-only is simply one endpoint
of the same search.

LIMITATION
----------
This is an educational unweighted-RMSE parameter scan, not the full
Pantheon+ covariance-based cosmological likelihood.

The supernova data constrain expansion history; they do not directly
test extra dimensions.
"""

    (RESULT_DIR / "results.txt").write_text(text)
    print(text)
    print(f"Full scan saved to: {RESULT_DIR / 'omega_scan.csv'}")
    print(f"Figures saved to: {FIG_DIR}")
    print(f"Results saved to: {RESULT_DIR}")


if __name__ == "__main__":
    main()
