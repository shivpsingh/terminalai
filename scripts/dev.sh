#!/usr/bin/env bash
set -euo pipefail
uv pip install -e .[dev]
ruff check .
mypy src
pytest -q
