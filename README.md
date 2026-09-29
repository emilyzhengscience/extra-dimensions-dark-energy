# Supernova Evidence for Dark Energy

### A Data Analysis Project Inspired by Greene and Levin

This project uses real Type Ia supernova observations to investigate evidence for dark-energy-like cosmic expansion.

The project is inspired by Brian Greene and Janna Levin's paper **"Dark Energy and Stabilization of Extra Dimensions"**, which investigates whether vacuum effects associated with compact extra dimensions could help stabilize those dimensions while producing an effective energy that behaves like dark energy.

Rather than attempting to reproduce the advanced theoretical calculations in the paper, this project focuses primarily on **real observational data analysis**.

The main goal is to determine whether Type Ia supernova observations are better described by a simple matter-only universe or by a universe containing a dark-energy-like component.

---

## Research Question

> **Can real Type Ia supernova observations distinguish between a matter-only universe and a universe containing dark energy?**

A secondary question is:

> **How does this observational evidence connect to Greene and Levin's proposal that stabilization of extra dimensions could produce positive vacuum energy?**

The project does **not** attempt to prove that extra dimensions exist or that they cause dark energy.

---

## Data

The project will use the public **Pantheon+ Type Ia supernova dataset**.

Type Ia supernovae can be used as distance indicators because their observed brightness allows astronomers to estimate their distance.

Two important quantities in the dataset are:

- **Redshift** $z$, which is related to the expansion of the Universe.
- **Distance modulus** $\mu$, which represents the inferred distance to a supernova.

The primary analysis will examine how measured supernova distance changes with redshift.

---

## 1. Explore the Observational Data

The first step is to load and examine the Pantheon+ data using Python.

The analysis will investigate questions such as:

- How many supernova observations are included?
- What range of redshifts is covered?
- How are the observations distributed across redshift?
- How does distance modulus change with redshift?
- What are the typical observational uncertainties?

The first major result will be a **Hubble diagram** showing observed distance modulus as a function of redshift.

```math
\mu_{\mathrm{observed}} \quad \text{vs.} \quad z
```

This allows the expansion history of the Universe to be examined directly from observational data.

---

## 2. Compare Two Simple Cosmological Models

The observational data will be compared with two simple cosmological models.

### Model A: Matter-Only Universe

```math
\Omega_m = 1,
\qquad
\Omega_\Lambda = 0
```

This model contains matter but no dark energy.

### Model B: Matter + Dark Energy

A simple standard dark-energy model will use approximately

```math
\Omega_m = 0.3,
\qquad
\Omega_\Lambda = 0.7.
```

For a spatially flat universe, the expansion rate can be written as

```math
H(z)
=
H_0
\sqrt{
\Omega_m(1+z)^3+\Omega_\Lambda
}.
```

The luminosity distance is calculated numerically from

```math
d_L(z)
=
(1+z)c
\int_0^z
\frac{dz'}{H(z')}.
```

The predicted distance modulus is then

```math
\mu(z)
=
5\log_{10}
\left(
\frac{d_L}{\mathrm{Mpc}}
\right)+25.
```

The purpose of these equations is not to derive cosmology from first principles, but to generate predictions that can be compared with real observations.

---

## 3. Compare Predictions with Real Data

The predictions from both models will be plotted together with the Pantheon+ observations.

This allows a direct comparison between

```math
\text{real supernova observations}
```

and

```math
\text{matter-only prediction}
```

and

```math
\text{matter + dark-energy prediction}.
```

The goal is to determine which expansion history more closely follows the observed supernova distances.

---

## 4. Analyze the Residuals

Visual comparison alone is not enough.

For each supernova, the residual between the observation and a model prediction will be calculated:

```math
r_i
=
\mu_{\mathrm{observed},i}
-
\mu_{\mathrm{model},i}.
```

If a model describes the observations well, its residuals should remain relatively close to zero without a strong systematic trend.

Residuals will therefore be plotted as a function of redshift:

```math
r(z)
=
\mu_{\mathrm{observed}}(z)
-
\mu_{\mathrm{model}}(z).
```

The residual patterns of the two cosmological models can then be compared.

---

## 5. Quantify the Model Difference

A simple numerical measure will be used to summarize how closely each model follows the observations.

One possible measure is the root mean squared error:

```math
\mathrm{RMSE}
=
\sqrt{
\frac{1}{N}
\sum_{i=1}^{N}
\left(
\mu_i-\mu_{\mathrm{model},i}
\right)^2
}.
```

The two values

```math
\mathrm{RMSE}_{\mathrm{matter}}
```

and

```math
\mathrm{RMSE}_{\mathrm{dark\ energy}}
```

will be compared.

A smaller residual error indicates that the corresponding model follows the observed distance-redshift relation more closely.

If time permits, observational uncertainties can also be incorporated into a more formal statistical comparison.

---

## Connection to Greene and Levin

The main part of this project is observational data analysis.

Greene and Levin's work provides a theoretical motivation for asking where dark-energy-like vacuum energy might come from.

In models with compact extra dimensions, let $b$ represent the size of an extra dimension and let $V(b)$ represent its effective potential.

A stable size $b_0$ requires

```math
V'(b_0)=0
```

and

```math
V''(b_0)>0.
```

If the stabilized configuration also has

```math
V(b_0)>0,
```

then positive vacuum energy remains after stabilization.

Conceptually, the connection is

```math
\text{extra-dimensional physics}
\rightarrow
\text{stabilization}
\rightarrow
\text{positive vacuum energy}
\rightarrow
\text{dark-energy-like behavior}.
```

The Pantheon+ analysis in this project investigates the **observational phenomenon that dark energy is used to explain**.

It does not directly test the existence of extra dimensions.

---

## Project Workflow

The main analysis follows a short data-driven workflow:

```math
\text{Pantheon+ data}
\rightarrow
\text{Hubble diagram}
\rightarrow
\text{two cosmological models}
\rightarrow
\text{residuals}
\rightarrow
\text{model comparison}.
```

The results are then connected conceptually to the physical mechanism discussed by Greene and Levin.

---

## Expected Figures

The project will focus on a small number of interpretable figures.

### Figure 1 — Supernova Redshift Distribution

Distribution of Pantheon+ observations across redshift.

### Figure 2 — Hubble Diagram

Observed Pantheon+ supernova distances together with predictions from:

- a matter-only model;
- a matter + dark-energy model.

### Figure 3 — Residual Analysis

Residuals between observed and predicted distance modulus as a function of redshift.

### Figure 4 — Model Error Comparison

Comparison of the residual error for the two cosmological models.

---

## Project Scope

This is designed as a short computational physics and data-analysis project.

The primary work is:

**real data analysis → visualization → model comparison → interpretation**

Only the mathematical and physical concepts needed to understand the analysis will be introduced.

The project will **not** attempt to:

- derive the Friedmann equations;
- reproduce the Greene-Levin Casimir-energy calculation;
- solve higher-dimensional Einstein equations;
- fit an extra-dimensional model directly to observations;
- perform a large cosmological parameter search;
- reproduce the full Pantheon+ cosmological analysis;
- prove that extra dimensions are responsible for dark energy.

These topics are outside the scope of this mini-project.

---

## Suggested Repository Structure

```text
extra-dimensions-dark-energy/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── notebooks/
│   ├── 01_explore_pantheon.ipynb
│   └── 02_compare_cosmological_models.ipynb
│
├── data/
│   └── README.md
│
├── figures/
│
└── docs/
    └── project_notes.md
```

Only two main notebooks are required.

---

## Tools

- Python
- Jupyter Notebook
- NumPy
- Pandas
- SciPy
- Matplotlib

No machine-learning model is required for the core project.

---

## Four-Week Schedule

| Week | Main Task |
| --- | --- |
| **1** | Understand the basic concepts of redshift, supernova distance, and dark energy; load and explore Pantheon+ |
| **2** | Create the Hubble diagram and implement the two simple cosmological models |
| **3** | Calculate residuals and compare the models |
| **4** | Interpret the results, connect them to Greene-Levin, and prepare the final report |

Because the analysis is intentionally limited in scope, much of the project time can be spent understanding and explaining the results rather than learning advanced theory.

---

## Main Scientific Limitation

This project tests whether real Type Ia supernova observations are better described by different simple cosmic expansion histories.

It does **not** observationally test extra dimensions.

The connection to Greene and Levin is theoretical:

```math
\text{observed accelerated expansion}
\longrightarrow
\text{need for a dark-energy-like component}
\longrightarrow
\text{possible physical origins}
\longrightarrow
\text{extra-dimensional stabilization}.
```

The distinction between **observational evidence** and a **possible theoretical explanation** is an important part of the project.

---

## Reference

B. R. Greene and J. Levin, **"Dark Energy and Stabilization of Extra Dimensions,"** *Journal of High Energy Physics* **11** (2007) 096, arXiv:0707.1062.

Pantheon+ Collaboration, public Type Ia supernova cosmology data release.

---

## License

Code developed for this project is released under the **MIT License**.

Third-party papers and datasets retain their original copyrights, licenses, and citation requirements.
