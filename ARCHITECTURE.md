# Architecture

One deployment defines one immutable title, goal, rulebook, and per-address attempt limit. `play` normalizes a proposed action and loophole rationale, rejects exact content reuse, and asks the leader plus every validator to classify the same frozen attempt. Validators independently repeat the classification and must agree exactly on the closed verdict.

Points are never chosen by an LLM: deterministic code maps `LEGAL_SUCCESS` to 3, `LEGAL_PARTIAL` to 1, and all other verdicts to 0. Only after consensus does the contract store the attempt and update bounded indexes, player score, and aggregate counters.

There is no frontend, backend, web source, token, or prize custody.
