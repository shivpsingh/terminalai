# Architecture Overview

Aegis Code is built as a modular monolith where each subsystem has explicit interfaces.

```text
CLI -> Orchestrator -> {Context Compiler, Agent Layer, Tool Runtime, Policy, Storage, Observability}
                             ^             |             |         |        |
                             +-------------+-------------+---------+--------+
```

Why this shape:
- clear boundaries now
- easy extraction later
- practical for a startup MVP
