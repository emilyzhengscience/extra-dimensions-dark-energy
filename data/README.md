# Data

The analysis uses the official Pantheon+SH0ES public data table:

`Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat`

Run:

```bash
python scripts/download_data.py
```

The downloaded third-party data file is intentionally not committed by default.
It remains subject to the Pantheon+ project's own terms and citation requirements.

Columns used by the student analysis:

- `zHD`: Hubble-diagram redshift
- `m_b_corr`: corrected/standardized SN Ia apparent magnitude
- `IS_CALIBRATOR`: used to exclude Cepheid calibrators from the Hubble-flow comparison
