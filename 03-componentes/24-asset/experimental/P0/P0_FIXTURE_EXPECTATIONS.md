# Asset PRO — P0 Fixture Expectations

**Status:** WORKING / NON-NORMATIVE  
**Pilot:** P0  
**Date:** 2026-10-02

---

## 1. Purpose

Define the regression fixtures required before ASSET-P0-001 can reach Execution Freeze.

## 2. Synthetic Golden Fixture

The synthetic fixture SHALL define 48 expected hourly slots covering two complete UTC days.

It SHALL deliberately include:

- one missing 1h interval;
- one extreme but OHLC-valid price observation;
- standard valid intervals around the anomalies;
- multiple 4h boundaries;
- one Daily transition;
- a checkpoint/restart location before the second UTC day.

Expected outputs SHALL explicitly freeze:

- detected missing-interval flag;
- detected extreme-observation flag;
- derived 4h completeness/incompleteness states;
- Daily completeness/incompleteness states;
- canonical serialized output;
- expected hashes.

The synthetic fixture is designed to test handling rules and therefore is not required to be a complete market series.

## 3. Real Golden Fixture

Planned source:

- Binance Public Data;
- Binance Spot;
- BTCUSDT;
- 1h klines.

Planned period:

- start: 2024-12-31 00:00 UTC inclusive;
- end: 2025-01-03 00:00 UTC exclusive.

This three-day fixture intentionally crosses 2025-01-01, when the Binance Spot public-data archive changes timestamp units from milliseconds to microseconds.

The normalized fixture SHALL use canonical epoch microseconds regardless of source-unit differences.

Expected complete interval slots: 72, subject to source validation.

## 4. Real Validation Dataset

The main ASSET-P0-001 validation dataset is separate from the fixture:

- BTCUSDT Binance Spot;
- native 1h;
- 2025-01-01 through 2025-04-01 UTC exclusive;
- expected 2160 contiguous 1h intervals;
- derived 4h and 1d series.

Large validation datasets SHALL normally remain outside Git and be referenced using:

- Dataset ID;
- Data Version;
- provenance;
- checksum;
- reconstruction/access instructions.

## 5. Data Feed Ownership

Fixture bytes and canonical dataset manifests are producer-side artifacts and belong to the `crypto-pro-datafeed` experimental package.

## 6. Freeze Requirement

No fixture is considered Golden until:

- bytes are generated/acquired;
- expected outputs are independently reviewed;
- canonical hashes are recorded;
- the Data Feed commit containing the fixture metadata is pinned.

