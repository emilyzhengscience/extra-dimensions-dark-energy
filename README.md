# Supernova Evidence for Dark Energy

### A Data-Analysis Project Inspired by Greene and Levin

This project uses real **Pantheon+ Type Ia supernova observations** to ask:

> **Do observed supernova distances follow a matter-only expansion history, or are they better described by a universe containing a dark-energy-like component?**

The project is inspired by Brian R. Greene and Janna Levin's paper **"Dark Energy and Stabilization of Extra Dimensions."** The emphasis here is on **real data analysis**. Extra-dimensional physics is used only as motivation after the observational result is understood.

---

## 1. The project in plain language

For each Type Ia supernova, Pantheon+ provides measurements including:

- **redshift** `zHD` — related to how much cosmic expansion stretched its light;
- **corrected standardized magnitude** `m_b_corr` — a standardized brightness measurement.

The analysis follows this logic:

```text
real observations
      ↓
a cosmological model predicts brightness versus redshift
      ↓
observation - prediction = residual
      ↓
combine many residuals into RMSE
      ↓
compare models
      ↓
vary a model parameter to find the smallest RMSE
```

The current selection uses **1,580 Hubble-flow light-curve entries** from the 1,701-row released Pantheon+ table.

---

## 2. What are Omega_m and Omega_Lambda?

Cosmologists use density parameters, written with the Greek letter Omega (`Ω`):

```math
\Omega_i=\frac{\rho_i}{\rho_{\mathrm{critical}}}.
```

### Matter: Omega_m

```math
\Omega_m
```

is the **matter density parameter**. It includes ordinary matter and dark matter.

For example,

```math
\Omega_m=0.30
```

means the matter density is 30% of the critical density.

### Dark energy: Omega_Lambda

```math
\Omega_\Lambda
```

is the density parameter associated here with a **cosmological constant**, the simplest dark-energy model.

For example,

```math
\Omega_\Lambda=0.70
```

means the cosmological-constant energy density is 70% of the critical density.

---

## 3. Why do they add to 1?

This mini-project assumes a **spatially flat universe** and neglects radiation for this introductory analysis.

Therefore,

```math
\Omega_m+\Omega_\Lambda=1.
```

Once `Ωm` is chosen, `ΩΛ` is fixed:

```math
\Omega_\Lambda=1-\Omega_m.
```

Example:

```math
\Omega_m=0.351
```

gives

```math
\Omega_\Lambda=1-0.351=0.649.
```

This is a model assumption, not something imposed by the supernova data alone:

```math
\text{data}+\text{model assumptions}
\longrightarrow
\text{parameter estimate}.
```

---

## 4. Two starting models

### Model A — Matter only

```math
\Omega_m=1,\qquad\Omega_\Lambda=0.
```

### Model B — Matter + dark energy

```math
\Omega_m=0.3,\qquad\Omega_\Lambda=0.7.
```

The question is simply:

> **Which model's predictions lie closer to the real Pantheon+ observations?**

---

## 5. How does a model make a prediction?

For this simplified flat matter + cosmological-constant model,

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

The predicted standardized magnitude has the form

```math
m_{\mathrm{model}}(z)
=
5\log_{10}D_L(z)+\mathcal{M}.
```

The code fits the common offset `Mcal` for each model. This allows the project to compare the **shape** of the Hubble diagram without letting an arbitrary overall magnitude/Hubble-scale offset determine the answer.

The student does not need to derive these equations from general relativity. The key idea is:

> **Different values of `Ωm` produce different expansion histories, which produce different predicted supernova brightness-versus-redshift curves.**

---

## 6. What is a residual?

A residual is:

```math
\text{residual}=\text{observation}-\text{prediction}.
```

For this project,

```math
r_i=m_{\mathrm{observed},i}-m_{\mathrm{model},i}.
```

Example:

```math
m_{\mathrm{observed}}=22.10,\qquad
m_{\mathrm{model}}=21.90
```

so

```math
r=22.10-21.90=+0.20\ \mathrm{mag}.
```

A good model should generally have residuals close to zero without a strong systematic trend with redshift.

---

## 7. What is RMSE?

There are 1,580 observations, so there are 1,580 residuals. We need one simple number that summarizes their overall size.

**RMSE** means **Root Mean Squared Error**:

```math
\mathrm{RMSE}
=
\sqrt{\frac{1}{N}\sum_{i=1}^{N}r_i^2}.
```

The name describes the calculation:

1. calculate each **error** (residual);
2. **square** it so positive and negative errors cannot cancel;
3. take their **mean**;
4. take the square **root** to return to magnitude units.

Example residuals:

```math
+1,\quad -2,\quad +3
```

become

```math
1^2,\quad(-2)^2,\quad3^2
=
1,\quad4,\quad9.
```

Therefore,

```math
\mathrm{RMSE}
=
\sqrt{\frac{1+4+9}{3}}
\approx2.16.
```

A useful intuition is:

> **RMSE summarizes the typical scale of the model's prediction error. Smaller is better.**

---

## 8. Results from the successful reference run

```text
Rows in released table:          1701
Rows in selected Hubble sample:  1580
Redshift range:                  0.01016 to 2.26137
```

| Model | `Ωm` | `ΩΛ` | RMSE |
| --- | ---: | ---: | ---: |
| Matter only | 1.0 | 0.0 | 0.2113 mag |
| Matter + dark energy | 0.3 | 0.7 | 0.1539 mag |

Because

```math
0.1539<0.2113,
```

the matter + dark-energy model follows the observed Hubble-diagram shape more closely in this simplified comparison.

---

## 9. Let the data comparison choose Omega_m

Instead of testing only `Ωm = 0.3`, the program varies `Ωm`.

For every trial value:

```text
choose Ωm
   ↓
ΩΛ = 1 - Ωm
   ↓
calculate the predicted Hubble diagram
   ↓
fit the common magnitude offset
   ↓
calculate residuals
   ↓
calculate RMSE
   ↓
try another Ωm
```

The program searches for:

```math
\boxed{\Omega_m\ \text{that minimizes RMSE}}.
```

The successful reference run found:

```math
\Omega_m\approx0.35114,
```

so flatness gives

```math
\Omega_\Lambda
=
1-\Omega_m
\approx0.64886.
```

The corresponding simplified RMSE was

```math
\mathrm{RMSE}\approx0.15305\ \mathrm{mag}.
```

This is a basic example of **parameter estimation / model fitting**:

> The program is not told that `Ωm` should be about 0.35. It changes the parameter, compares each model with the observations, and finds where the mismatch becomes smallest.

---

## 10. Figures

The analysis generates five figures.

### Figure 1 — Redshift distribution

Shows where the Pantheon+ observations lie in redshift.

### Figure 2 — Hubble diagram

Shows real observations together with the matter-only and matter + dark-energy predictions.

### Figure 3 — Residuals

Plots

```math
m_{\mathrm{observed}}-m_{\mathrm{model}}
```

against redshift so systematic model errors are easier to see.

### Figure 4 — Fixed-model RMSE

Directly compares the RMSE of the two starting models. Smaller is better.

### Figure 5 — RMSE versus Omega_m

This visualizes the parameter-fitting process.

The horizontal axis is `Ωm`. Because flatness is assumed,

```math
\Omega_\Lambda=1-\Omega_m.
```

The vertical axis is RMSE.

The plot marks:

- `Ωm = 1.0`: matter-only model;
- `Ωm = 0.3`: representative dark-energy model;
- `Ωm ≈ 0.351`: minimum RMSE in the simplified fit.

The minimum shows visually where the fitted parameter comes from.

---

## 11. Connection to Greene and Levin

Everything above is primarily **observational data analysis**.

Greene and Levin address a deeper theoretical question:

> **If observations favor an expansion history containing a dark-energy-like component, what underlying physics could produce positive vacuum energy?**

Their paper studies compact extra dimensions and Casimir energy.

If `b` represents the size of an extra dimension and `V(b)` its effective potential, stabilization requires

```math
V'(b_0)=0,\qquad V''(b_0)>0.
```

If

```math
V(b_0)>0,
```

the stabilized configuration can retain positive vacuum energy.

The conceptual connection is:

```text
Pantheon+ observations
        ↓
expansion-history comparison
        ↓
dark-energy-like component
        ↓
where could this energy come from?
        ↓
Greene-Levin extra-dimensional mechanism
```

Pantheon+ does **not** directly test extra dimensions.

---

## 12. Scientific limitations

The fitted result should be described as:

> **Within our simplified flat matter + Lambda model, the value of `Ωm` that minimized the unweighted RMSE was approximately 0.351, corresponding to `ΩΛ ≈ 0.649`.**

It should not be described as:

> "We measured the Universe to be exactly 35.1% matter and 64.9% dark energy."

This introductory analysis assumes:

- spatial flatness;
- matter + cosmological constant;
- negligible radiation for this exercise;
- a fitted common magnitude offset;
- unweighted RMSE as the introductory comparison statistic.

A publication-level Pantheon+ analysis uses statistical and systematic covariance information and a formal likelihood.

---

## 13. Run the project

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_data.py
python scripts/analyze.py
```

---

## 14. Repository structure

```text
extra-dimensions-dark-energy/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── scripts/
│   ├── download_data.py
│   └── analyze.py
├── figures/
│   ├── 01_redshift_distribution.png
│   ├── 02_hubble_diagram.png
│   ├── 03_residuals.png
│   ├── 04_model_comparison.png
│   └── 05_rmse_vs_omega_m.png
└── results/
    ├── README.md
    ├── model_comparison.csv
    ├── omega_scan.csv
    └── results.txt
```

## References

B. R. Greene and J. Levin, **"Dark Energy and Stabilization of Extra Dimensions,"** *Journal of High Energy Physics* **11** (2007) 096, arXiv:0707.1062.

Pantheon+SH0ES public Type Ia supernova data release.

D. Brout et al., **"The Pantheon+ Analysis: Cosmological Constraints,"** *The Astrophysical Journal* **938**, 110 (2022).

## License

Original code in this repository is released under the MIT License. Pantheon+ data and third-party papers retain their original terms and citation requirements.
