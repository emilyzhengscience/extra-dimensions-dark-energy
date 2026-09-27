# Dark Energy and Stabilization of Extra Dimensions

### A Computational Physics Mini-Project

This project explores a question inspired by Brian Greene and Janna Levin's 2007 paper **“Dark Energy and Stabilization of Extra Dimensions”**:

> **Can stabilization of compact extra dimensions produce an effective vacuum energy that behaves like dark energy?**

The project uses a simplified mathematical model, numerical simulations, public cosmological data, and a small machine-learning experiment. The goal is not to reproduce the full higher-dimensional quantum field theory of the original paper, but to investigate its central physical idea in a computationally accessible way.

## Physics Model

We describe the size of a compact extra dimension by \(b(t)\) and introduce an effective potential

\[
V(b).
\]

A stable extra dimension corresponds to a minimum of this potential:

\[
V'(b_0)=0,
\qquad
V''(b_0)>0.
\]

If the extra dimension stabilizes at \(b_0\) while

\[
V(b_0)>0,
\]

the remaining approximately constant vacuum energy can behave like dark energy in the four-dimensional Universe.

The central idea is therefore

\[
\boxed{
\text{extra dimension}
\rightarrow
\text{stabilization}
\rightarrow
V(b_0)>0
\rightarrow
\text{dark-energy-like behavior}
}
\]

## What This Project Will Do

1. **Build a simplified stabilization potential** \(V(b)\) inspired by Casimir-energy models.

2. **Find stable extra-dimensional configurations** using

\[
V'(b_0)=0,
\qquad
V''(b_0)>0.
\]

3. **Simulate the dynamics of the extra dimension** using a simplified equation such as

\[
\ddot b+3H\dot b+V'(b)=0.
\]

4. **Compare the resulting cosmology with real observations** using the public **Pantheon+ Type Ia supernova dataset**.

5. **Use a simple machine-learning model** to explore which regions of parameter space produce stable solutions.

## Main Research Question

> **Can a simplified model of stabilized extra dimensions generate dark-energy-like behavior consistent with the observed expansion history of the Universe?**

## Tools

- Python
- NumPy
- SciPy
- Pandas
- Matplotlib
- scikit-learn
- Jupyter Notebook

## Data

The observational component will use the publicly available **Pantheon+ Type Ia supernova dataset**.

The supernova distance-redshift relation will be compared with theoretical predictions calculated from

\[
H(z),
\qquad
d_L(z),
\qquad
\mu(z).
\]

## Expected Outputs

The project will produce:

- plots of the extra-dimensional potential \(V(b)\);
- numerical simulations of stabilization \(b(t)\);
- a stability map of model parameter space;
- a Pantheon+ supernova Hubble diagram;
- a small machine-learning parameter study;
- a short final research report.

## Scope

This is a **four-week computational physics project**. It does not attempt to reproduce the full quantum-field-theory or
