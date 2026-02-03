# LOOCV-LROCV

Small utilities for running **LOOCV** (Leave-One-Out Cross-Validation) and **LROCV** (Leave-*r*-Out Cross-Validation) experiments in Python.

This repo is intentionally lightweight: it contains a small Python package (`loocv_lrocv/`), tests, and a Jupyter notebook demonstrating experiments.
---

## What are LOOCV and LROCV?

Cross-validation evaluates how well a model generalizes by repeatedly training on a subset of the data and testing on held-out samples.

### LOOCV (Leave-One-Out Cross-Validation)

- If you have **n** samples, LOOCV runs **n folds**.
- In each fold, **1 sample** is the test set and the remaining **n − 1** samples are the training set.
- Each sample is used once as a singleton test set.
- In scikit-learn terms, LOOCV is equivalent to `KFold(n_splits=n)` and `LeavePOut(p=1)`.

**Why use it?**
- It uses almost all data for training each time, which is helpful for **small datasets**.
- It is deterministic given the data ordering.

**Trade-offs**
- It is **computationally expensive** because it trains **n models** (one per sample). - Because each test set is only one point, the estimate can have **high variance** for some problems (one “hard” point can swing the score).

---

### LROCV (Leave-*r*-Out Cross-Validation)

LROCV generalizes LOOCV by leaving out **r** samples per fold:

- For **n** samples and leave-out size **r**, each fold tests on a distinct subset of size **r**.
- This produces **all combinations** of size **r**, i.e. \(\binom{n}{r}\) folds in total.
- In scikit-learn, this matches the *idea* of `LeavePOut(p=r)` (a leave-*p*-out iterator).

**Why use it?**
- Compared to LOOCV, leaving out more samples can sometimes provide a more “stable” estimate for certain tasks (because each test fold is larger).

**Trade-offs**
- LROCV becomes **combinatorially expensive** very quickly: \(\binom{n}{r}\) grows fast.
  - Example: n=30, r=2 → 435 folds; n=30, r=5 → 142506 folds.

---

## When should you use these?

Use LOOCV/LROCV when:

- Your dataset is **small**, and you want to use as much data as possible for training each fold.
- You can afford the runtime cost.

Avoid (or adapt) these methods when:

- Your data has **grouping / leakage risk** (e.g., multiple samples from the same subject). In that case, consider group-aware CV such as `LeaveOneGroupOut`.
- Your data is **time-ordered** (time series), where standard leave-out CV can leak future information. (Prefer time-series splits.)

---

## Repository contents

- `loocv_lrocv/` — the Python package (core utilities live here).
- `LOOCV_LROCV.ipynb` — notebook with example experiments / usage.
- `tests/` — tests for the package.
- `pyproject.toml` — packaging/build configuration.
- `requirements.txt` / `requirements-dev.txt` — runtime and dev dependencies.

---

## Installation

From the repository root:

```bash
pip install .
```

For local development:

```bash
pip install -e .
```

---

## Quickstart

The easiest way to see how to run the experiments is to open the notebook:

- `LOOCV_LROCV.ipynb`

Run it with Jupyter:

```bash
pip install -r requirements.txt
jupyter notebook
```

Then open `LOOCV_LROCV.ipynb`.

---

## Development

Install dev dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest
```

If you use pre-commit (repo includes `.pre-commit-config.yaml`):

```bash
pre-commit install
pre-commit run --all-files
```

---

## License

No license file is currently present in the repository root.
