# Asset PRO — P0 Causal Replay Specification

**Status:** WORKING / NON-NORMATIVE  
**Pilot:** P0  
**Date:** 2026-10-02

---

## 1. Purpose

Define the causal replay contract used to expose historical market data to future Asset PRO analytical methods without look-ahead.

## 2. Replay Clock

The harness SHALL maintain one logical `replay_timestamp`.

At timestamp `t`, an analytical consumer may access only observations whose required close/detection time is not later than `t`.

For closed candles:

`visible(candle, t) iff candle.close_time <= t`.

## 3. Closed-Candle Rule

By default, incomplete candles SHALL NOT be exposed as finalized candles.

A higher-timeframe candle becomes available only after its own close boundary is reached.

Example: a Daily candle may not expose its final High/Low/Close to a 4h replay during the same unfinished day.

## 4. Interface

Conceptual sequence:

`initialize → reveal next closed observation → update consumer state → emit snapshot/events → advance clock`.

The replay layer SHALL NOT provide arbitrary access to future dataset rows.

## 5. Snapshot Envelope

A snapshot SHALL preserve at least:

- experiment_id;
- replay_timestamp;
- dataset_id;
- data_version;
- method_version;
- code_version;
- parameter_profile;
- state_schema_version;
- module_state;
- data_quality_state;
- last_event_id;
- snapshot hash.

## 6. Event Log

Events SHALL be append-only and preserve at least:

- event_id;
- experiment_id;
- event_type;
- event_timestamp;
- detection_timestamp;
- timeframe;
- asset/market reference;
- source/evidence references where applicable;
- prior/resulting state references;
- data-quality flags;
- method/code/profile identity.

Historical events are not silently rewritten.

## 7. Checkpoint/Restart

A continuous replay and a replay interrupted at a saved checkpoint then resumed SHALL produce equivalent deterministic outputs under identical identities.

## 8. Canonical Serialization

Deterministic hash comparison requires a frozen canonical serialization rule covering:

- field order;
- timestamp format;
- decimal representation;
- encoding;
- newline policy;
- ordering of semantically unordered collections.

The concrete serialization format is TBD before P0 execution.
