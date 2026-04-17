"""Test fixtures."""

from pathlib import Path

import pytest

from aegis_code.storage.db import Database


@pytest.fixture
def test_db(tmp_path: Path) -> Database:
    db = Database(f"sqlite+pysqlite:///{tmp_path / 'test.db'}")
    db.create_all()
    return db
