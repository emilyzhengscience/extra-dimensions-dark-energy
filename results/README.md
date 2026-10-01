# Generated Results

This version performs a full parameter scan rather than starting with a preselected 0.3/0.7 model.

`omega_scan.csv` contains all 1,001 trials:

```text
Omega_m = 0.000, 0.001, ... , 1.000
```

For every trial:

```text
Omega_Lambda = 1 - Omega_m
```

The best tested model is simply the row with the smallest `RMSE_mag`.

`model_comparison.csv` summarizes only the discovered best model and the matter-only endpoint.
