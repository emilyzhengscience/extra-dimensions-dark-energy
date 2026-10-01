# Supernova Evidence for Dark Energy

### A Data Analysis Project Inspired by Greene and Levin

## Research Question

> **Can real Type Ia supernova observations distinguish between a matter-only universe and a universe containing dark energy?**

This project uses the public **Pantheon+ Type Ia supernova dataset** to compare observed supernova brightnesses with predictions from simple cosmological models.

It is inspired by Brian R. Greene and Janna Levin's paper **"Dark Energy and Stabilization of Extra Dimensions"**. The supernova analysis does **not** test extra dimensions directly. Instead, it first asks whether the observations support an expansion history containing a dark-energy-like component. The Greene-Levin paper is then used to discuss one possible theoretical origin of positive vacuum energy.

---

## 1. What Do We Observe?

Type Ia supernovae can be standardized so that their observed brightness provides information about distance. For each supernova, Pantheon+ provides quantities including:

- `zHD`: redshift used for the Hubble diagram
- `m_b_corr`: corrected standardized apparent magnitude
- `IS_CALIBRATOR`: whether the object is a SH0ES calibrator

For this project, the Hubble-flow sample is selected using:

```text
zHD > 0.01
IS_CALIBRATOR == 0
```

The released table contains **1701 rows**, and this selection leaves **1580 observations**, spanning approximately

```math
0.01016 < z < 2.26137.
```

The basic observational question is simple:

> At each redshift, how closely does a cosmological model predict the observed supernova brightness?

---

## 2. The Cosmological Model

The project assumes a spatially flat universe containing matter and a cosmological-constant-like dark-energy component.

The density parameters are:

```math
\Omega_m = \text{matter density parameter}
```

and

```math
\Omega_\Lambda = \text{cosmological-constant (dark-energy) density parameter}.
```

`Omega_m` includes both ordinary matter and dark matter.

Under the flat-universe assumption used in this project,

```math
\Omega_m + \Omega_\Lambda = 1.
```

Therefore, once `Omega_m` is chosen,

```math
\Omega_\Lambda = 1-\Omega_m.
```

This is a **model assumption**, not something imposed by the supernova data themselves.

For a flat matter + cosmological-constant universe,

```math
E(z)=\frac{H(z)}{H_0}
=
\sqrt{\Omega_m(1+z)^3+\Omega_\Lambda}.
```

The dimensionless luminosity distance is

```math
D_L(z)
=
(1+z)\int_0^z\frac{dz'}{E(z')}.
```

The predicted standardized supernova magnitude can then be written as

```math
m_{\mathrm{model}}(z)
=
5\log_{10}D_L(z)+\mathcal{M}.
```

The constant `Mcal` is fitted separately for every model. It absorbs the unknown overall magnitude/Hubble-scale normalization, so the comparison is based mainly on the **shape of the Hubble diagram**, rather than an arbitrary vertical offset.

---

## 3. Observation vs. Prediction: Residuals

For every supernova, the code compares the observed magnitude with the model prediction.

The difference is called a **residual**:

```math
r_i
=
m_{\mathrm{observed},i}-m_{\mathrm{model},i}.
```

A residual near zero means the prediction is close to the observation.

Positive and negative residuals cannot simply be averaged because they could cancel each other. Instead, this project uses **Root Mean Square Error (RMSE)**:

```math
\mathrm{RMSE}
=
\sqrt{\frac{1}{N}\sum_{i=1}^{N}r_i^2}.
```

RMSE gives one number summarizing the typical size of the model's prediction errors.

**Smaller RMSE = closer agreement with the observed Hubble diagram.**

Residual plots are also examined because a single RMSE value can hide systematic patterns in the errors.

---

## 4. First Test: Two Fixed Cosmological Models

As an initial comparison, the analysis evaluates two models.

### Model A — Matter-only universe

```math
\Omega_m=1.0,
\qquad
\Omega_\Lambda=0.0.
```

Result:

```text
RMSE = 0.211276 mag
```

### Model B — Matter + dark energy

```math
\Omega_m=0.3,
\qquad
\Omega_\Lambda=0.7.
```

Result:

```text
RMSE = 0.153913 mag
```

The smaller RMSE of the second model shows that, in this simplified analysis, a model containing a dark-energy-like component follows the observed supernova Hubble diagram more closely than the matter-only model.

This comparison motivates a better question:

> Instead of choosing `Omega_m = 0.3` beforehand, can we let the supernova data determine which value gives the smallest error?

---

## 5. Scanning the Matter Density

The main numerical experiment scans **1001 possible values** of `Omega_m` from 0 to 1:

```text
0.000, 0.001, 0.002, ... , 0.999, 1.000
```

For every value:

1. Set `Omega_m` to the scanned value.
2. Use flatness to calculate

```math
\Omega_\Lambda=1-\Omega_m.
```

3. Calculate the predicted luminosity distance for every supernova.
4. Fit the common magnitude offset `Mcal`.
5. Calculate all residuals.
6. Calculate the RMSE.
7. Compare that RMSE with the values from all other scanned models.

The best scanned model is simply the row with the **lowest RMSE**.

---

## 6. Main Result

The minimum of the 1001-point scan occurs at

```math
\boxed{\Omega_m=0.351}
```

and therefore, under the flat-universe assumption,

```math
\boxed{\Omega_\Lambda=0.649}.
```

The corresponding error is

```math
\boxed{\mathrm{RMSE}=0.1530481593\ \mathrm{mag}}.
```

Values around the minimum are:

| `Omega_m` | `Omega_Lambda` | RMSE (mag) |
|---:|---:|---:|
| 0.350 | 0.650 | 0.153048552 |
| **0.351** | **0.649** | **0.153048159** |
| 0.352 | 0.648 | 0.153048385 |
| 0.353 | 0.647 | 0.153049227 |
| 0.354 | 0.646 | 0.153050682 |

The RMSE decreases as the scan approaches `Omega_m ≈ 0.351` and increases again after passing it. This produces a clear minimum in the RMSE-versus-`Omega_m` curve.

The important scientific logic is:

```math
\boxed{
\text{observations}
+
\text{model assumptions}
\longrightarrow
\text{parameter estimate}
}
```

The value `0.351` was **not chosen beforehand**. It emerged from comparing the scanned models with the Pantheon+ observations.

A continuous one-parameter minimization gives approximately

```math
\Omega_m \approx 0.35114,
\qquad
\Omega_\Lambda \approx 0.64886,
```

which is consistent with the minimum of the discrete scan.

### What this result does *not* mean

The correct interpretation is:

> **Within our simplified flat matter + Lambda model, the value of `Omega_m` that minimizes the unweighted RMSE is approximately 0.351, corresponding to `Omega_Lambda ≈ 0.649`.**

It should **not** be interpreted as a precision measurement that the Universe is exactly 35.1% matter and 64.9% dark energy. The result depends on the model assumptions and simplified statistical method used here.

---

## 7. Figures

The analysis generates figures that show different stages of the experiment:

```text
figures/
├── 01_redshift_distribution.png
├── 02_hubble_diagram.png
├── 03_residuals.png
├── 04_model_comparison.png
└── 05_rmse_vs_omega_m.png
```

### Figure 1 — Redshift distribution

Shows where the selected Pantheon+ observations lie in redshift.

### Figure 2 — Hubble diagram

Shows the observed standardized supernova magnitudes together with the predicted curves from the matter-only and dark-energy models.

### Figure 3 — Residuals

Shows observation-minus-prediction errors as a function of redshift. This helps reveal systematic differences that may be hidden by a single RMSE number.

### Figure 4 — Fixed-model comparison

Compares the RMSE of the matter-only model with the example matter + dark-energy model.

### Figure 5 — RMSE versus `Omega_m`

This is the central parameter-scan figure. It shows how the model-data error changes as `Omega_m` is varied from 0 to 1. The lowest point occurs near

```math
\Omega_m=0.351.
```

This figure visually demonstrates how the best-fitting parameter value is obtained from the data.

---

## 8. Connection to Greene and Levin

The observational part of this project finds that the Pantheon+ Hubble diagram is better described by a model containing a positive dark-energy-like component than by the simple matter-only model.

That leads to a deeper theoretical question:

> **If the Universe contains something behaving like positive vacuum energy, where could that energy come from?**

Greene and Levin's paper *Dark Energy and Stabilization of Extra Dimensions* investigates one possible answer involving compact extra dimensions.

Let `b` represent the size of a compact extra dimension and `V(b)` its effective potential.

A stable size `b_0` requires

```math
V'(b_0)=0
```

and

```math
V''(b_0)>0.
```

If the value of the effective potential at that stable point is positive,

```math
V(b_0)>0,
```

then the stabilized configuration can retain positive vacuum energy. Greene and Levin investigate how extra-dimensional Casimir effects can contribute to such stabilization and vacuum energy.

The conceptual chain connecting the two parts of this project is therefore:

```math
\text{Pantheon+ observations}
\rightarrow
\text{expansion-history test}
\rightarrow
\text{evidence for a dark-energy-like component}
\rightarrow
\text{question of its physical origin}
\rightarrow
\text{extra-dimensional stabilization as one theoretical possibility}.
```

### Important limitation

**The Pantheon+ supernova data do not detect extra dimensions and do not establish the Greene-Levin mechanism as the origin of dark energy.**

The observations and the theoretical paper answer different questions:

- **Pantheon+ analysis:** What expansion history is consistent with the observed supernova Hubble diagram?
- **Greene-Levin theory:** Could extra-dimensional physics provide a mechanism capable of producing positive vacuum energy?

The connection is therefore an interpretation and motivation, not a direct experimental test of extra dimensions.

---

## 9. Limitations

This is an educational data-analysis project rather than a publication-level cosmological parameter measurement.

Important simplifications include:

- spatial flatness is assumed;
- the model contains only matter and a cosmological constant for the late-time expansion calculation;
- radiation is neglected;
- dark energy is assumed to behave as a cosmological constant;
- the comparison uses an unweighted RMSE;
- the full Pantheon+ covariance matrix is not used;
- the analysis does not construct the complete Pantheon+ likelihood;
- Pantheon+ light-curve entries are treated directly rather than performing a full survey-level cosmological analysis.

A more advanced analysis could use the released covariance matrix and evaluate a statistic such as

```math
\chi^2
=
\Delta m^T C^{-1}\Delta m,
```

but that is beyond the intended scope of this mini-project.

---

## 10. Running the Project

Create a Python environment and install the required packages:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Download the official Pantheon+ data:

```bash
python scripts/download_data.py
```

Run the analysis:

```bash
python scripts/analyze.py
```

Generated output is written to:

```text
figures/
results/
```

---

## Repository Structure

```text
.
├── README.md
├── LICENSE
├── requirements.txt
├── data/
│   └── README.md
├── scripts/
│   ├── download_data.py
│   └── analyze.py
├── figures/
└── results/
```

---

## References

- B. R. Greene and J. Levin, *Dark Energy and Stabilization of Extra Dimensions*, JHEP 11 (2007) 096, arXiv:0707.1062.
- Pantheon+SH0ES public data release, `PantheonPlusSH0ES/DataRelease`.
- D. Brout et al., *The Pantheon+ Analysis: Cosmological Constraints*, The Astrophysical Journal 938, 110 (2022).

---

## License

Original code in this repository is released under the MIT License.

Pantheon+ data and third-party papers retain their original licenses, terms, and citation requirements.
