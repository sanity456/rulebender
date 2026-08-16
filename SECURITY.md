# Security and limitations

- All text is public, ASCII-bounded, and delimited as untrusted prompt data.
- The rulebook is prose, so common-mode model error remains possible even with independent replay.
- Exact verdict agreement fails closed but can reduce liveness on ambiguous attempts.
- `AMBIGUOUS` awards zero points and is not equivalent to illegality.
- Exact duplicate detection does not identify paraphrases or coordinated copying.
- Per-address limits are not Sybil-resistant; the leaderboard is recreational only.
- There are no prizes, time windows, owner moderation, or appeals encoded in v1.
- The contract does not generate hidden information; all actions become public after settlement.
