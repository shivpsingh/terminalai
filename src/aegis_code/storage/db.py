"""Database setup."""

from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from aegis_code.storage.tables import Base


class Database:
    """SQLite database wrapper."""

    def __init__(self, url: str = "sqlite+pysqlite:///aegis.db") -> None:
        self.engine = create_engine(url, future=True)
        self._session_factory = sessionmaker(
            bind=self.engine, class_=Session, expire_on_commit=False
        )

    def create_all(self) -> None:
        """Create all tables."""

        Base.metadata.create_all(self.engine)

    @contextmanager
    def session(self) -> Iterator[Session]:
        """Yield a transaction-scoped session."""

        with self._session_factory() as session:
            yield session
