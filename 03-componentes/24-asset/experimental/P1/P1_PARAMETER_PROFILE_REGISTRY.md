# Asset PRO — P1 Parameter Profile Registry

**Status:** DRAFT / NON-NORMATIVE  
**Experiment:** ASSET-P1-D1-001

---

# 1. General Rule

Parameter grids map behavior and search for plateaus. They do not search for maximum return.

All values must be frozen before their applicable phase is run.

---

# 2. M1 — Fixed-Window Pivot

## 4h

`w ∈ {2, 3, 4, 6, 8, 12}` bars

## Daily

`w ∈ {2, 3, 4, 5, 7, 10}` bars

Behavioral interpretation:

- smaller (w): Responsive;
- middle region: Balanced candidate;
- larger (w): Conservative.

These labels are descriptive, not ordinal quality rankings.

---

# 3. M2 — Fixed-Percentage Reversal

## 4h

`p ∈ {1.0%, 1.5%, 2.5%, 4.0%, 6.0%, 9.0%}`

## Daily

`p ∈ {2.0%, 3.0%, 5.0%, 8.0%, 12.0%, 18.0%}`

Primary basis:

- candidate extremum: High/Low;
- reversal confirmation: Close.

---

# 4. M3 — Volatility-Normalized Reversal

## DEV estimator screen

Fixed screening profile:

- window (n=14);
- multiplier (k=2.0);
- Close confirmation.

Estimators:

- E1 Wilder ATR;
- E2 Median True Range.

An estimator with a critical blocker is removed. If both survive, both may proceed.

## DEV full grid for surviving estimators

[
n \in \{10,14,21,34\}
]

[
k \in \{1.0,1.5,2.0,2.5,3.0,4.0\}
]

Primary confirmation remains Close-based.

### Diagnostic-only intrabar subset

DEV only:

- (n=14);
- (k \in \{1.5,2.0,3.0\}).

Diagnostic intrabar variants cannot become final candidates in ASSET-P1-D1-001. Material superiority/behavioral difference requires a future design revision, not silent promotion.

---

# 5. Structural Profiles

After detector-profile screening, surviving detector profiles feed a separate structural grid.

Equality tolerance:

[
q \in \{0.25,0.50,0.75\} \times ATR14
]

PCSB/reclaim break buffer:

[
b \in \{0,0.25,0.50\} \times ATR14
]

Trend-persistence requirement:

[
m \in \{2,3\}
]

where (m) is the minimum number of qualifying alternating directional swing-pair confirmations required to establish a directional trend.

Range minimum:

- at least two structural highs;
- at least two structural lows.

The structural grid therefore contains (3 × 3 × 2 = 18) profiles per surviving detector profile.

---

# 6. DEV Candidate Lock

For each method/timeframe:

1. remove profiles with critical blockers;
2. identify local parameter plateaus;
3. retain no more than three behaviorally distinct candidates when possible:
   - Responsive;
   - Balanced;
   - Conservative.

If fewer than three defensible candidates exist, retain only those that satisfy the rules.

No candidate is chosen by P&L, future return or visual preference.
