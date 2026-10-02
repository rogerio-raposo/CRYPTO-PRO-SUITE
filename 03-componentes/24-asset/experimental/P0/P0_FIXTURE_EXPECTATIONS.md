# Asset PRO — P0 Fixture Expectations

**Status:** WORKING / NON-NORMATIVE  
**Pilot:** P0  
**Date:** 2026-10-02

---

## 1. Purpose

Define the minimum regression fixtures required before P0 can be executed.

## 2. Synthetic Golden Fixture

A small fully auditable synthetic series SHALL include sufficient cases to test:

- valid OHLC records;
- deterministic ordering;
- at least one missing interval;
- at least one flagged extreme observation;
- a higher-timeframe boundary;
- a checkpoint/restart location;
- expected resampling outputs.

The fixture SHALL have frozen expected hashes/results after review.

## 3. Real Golden Fixture

A small immutable real-market sample SHALL test:

- source parsing;
- timestamp/boundary handling;
- native-to-derived resampling;
- provenance;
- canonical serialization.

It SHALL remain small enough for Git storage and review.

## 4. Historical Validation Dataset

The historical validation dataset is not a fixture.

Large validation datasets SHALL normally remain outside Git and be referenced using:

- Dataset ID;
- Data Version;
- provenance;
- checksum;
- reconstruction/access instructions.

## 5. Data Feed Ownership

Fixture bytes and canonical dataset manifests are producer-side artifacts and belong to the `crypto-pro-datafeed` experimental package.

## 6. Status

No fixture is frozen yet.
