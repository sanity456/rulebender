# RuleBender

RuleBender is a standalone, frontend-free GenLayer game. A deployer publishes a prose challenge; players submit actions and claimed loopholes. Independent validators classify each attempt, while deterministic contract code awards points and maintains the public scoreboard.

Write: `play`.

Views: `get_rulebook`, `get_attempt`, `get_attempt_count`, `get_attempt_id`, `get_player`, `get_player_count`, `get_player_id`, `get_stats`, `get_policy`.

```powershell
genvm-lint check contracts/rule_bender.py
python -m pytest tests/direct -v

# Terminal 1: start a five-validator GLSim network.
python tests/run_glsim.py --port 4000 --validators 5 --no-browser

# Terminal 2: run the integration suite while GLSim is running.
python -m pytest tests/integration -v -s
```

See `ARCHITECTURE.md`, `SECURITY.md`, `AUDIT.md`, and `evidence/` before deployment.
