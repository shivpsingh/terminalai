# Aegis Code

Aegis Code is a **terminal-first, local-first AI coding assistant harness** built in Python.

It teaches an architecture pattern for production-oriented coding agents:
- model does reasoning
- harness does orchestration, context assembly, tools, policy, memory, storage, and observability

## Why modular monolith first?
A small team can ship and learn faster with explicit in-process boundaries before splitting services.

## Architecture at a glance

```text
+--------------------------- User / CLI ---------------------------+
| aegis run | plan | resume | replay                              |
+------------------------------+------------------------------------+
                               |
                               v
+----------------------- Orchestration Layer ----------------------+
| lifecycle + state machine + checkpoints + recovery              |
+-------------+--------------------+----------------+---------------+
              |                    |                |
              v                    v                v
     +--------+------+    +--------+------+  +------+-------+
     | Context Compiler|    | Agent Layer   |  | Observability|
     | budget/select   |    | lead/worker   |  | logs/events  |
     +--------+------+    +--------+------+  +------+-------+
              |                    |                |
              +----------+---------+                |
                         v                          |
                +--------+--------+                 |
                | Model Adapters  |                 |
                | mock/local/cloud|                 |
                +--------+--------+                 |
                         |                          |
                         v                          v
                +--------+--------+        +--------+--------+
                | Tool Runtime    |------->| Storage (SQLite)|
                | policy + tools  |        | runs/events/etc |
                +-----------------+        +-----------------+
```

## Project layout
- `src/aegis_code/` main product code
- `tests/` educational unit + integration tests
- `docs/` architecture, ADRs, tutorials, reference
- `examples/` sample project and sample runs

## Quickstart
```bash
uv venv
uv pip install -e .[dev]
aegis plan "add logging around save"
aegis run "read README and summarize architecture"
pytest -q
ruff check .
mypy src
```

## Development commands
- `scripts/dev.sh` install and run checks
- `scripts/test.sh` run test suite

## Learning path
1. `docs/architecture/overview.md`
2. `docs/tutorials/how-a-run-works.md`
3. `src/aegis_code/orchestrator/service.py`
4. `src/aegis_code/tools/executor.py`
5. `docs/adr/*.md`

## Roadmap highlights
- richer worker parallelism
- robust sandbox backends
- IDE protocol bridge
- streaming model output and partial tool plans
