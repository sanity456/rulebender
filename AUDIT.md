# Security audit receipt

Review date: 2026-08-16

Status: reviewed testnet candidate. No critical, high, or medium-severity implementation defects were found in this engineering review. This is not an independent third-party certification.

## Reviewed artifact

- Contract: `contracts/rule_bender.py`
- Size: 13,350 bytes
- SHA-256: `6bbb630b0ebe2481ce2bc95d32155aa44a85f846582aec863900378c6b8bb92c`
- GenVM runner: pinned to `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`
- The retrieved StudioNet and Bradbury source bytes exactly match this artifact.

## Verification completed

- GenVM lint and SDK schema validation: pass; 9 views, 1 write, 4 constructor arguments.
- Strict Pyright type check: pass with zero diagnostics.
- Direct-mode tests: 11 passed, including attempt limits, exact duplicate prevention, deterministic scoring, index integrity, malformed output, and no-state-on-failure behavior.
- Five-validator GLSim tests: 1 complete consensus-scored attempt passed.
- Live StudioNet workflow: deployment and play `FINALIZED / MAJORITY_AGREE`; observed `LEGAL_SUCCESS`, 3 points.
- Live Bradbury workflow: deployment and play `ACCEPTED / AGREE / FINISHED_WITH_RETURN`; observed `LEGAL_SUCCESS`, 3 points.
- Dependency integrity: `pip check` passed. Repository secret scan found no wallet, keystore, mnemonic, password, or private-key material.

## Findings and residual risks

- Low: per-address attempt limits and scores are not Sybil-resistant. The scoreboard must remain recreational unless an identity layer is added.
- Informational: exact duplicate detection does not detect paraphrases or coordinated copying.
- Informational: prose rules admit common-mode model interpretation errors even with independent replay; exact verdict agreement is fail-closed.
- Informational: `AMBIGUOUS` deliberately awards zero points and must not be interpreted as an illegality finding.

Exact addresses, transaction hashes, status evidence, and workflow hashes are in `evidence/studionet.json` and `evidence/bradbury.json`.
