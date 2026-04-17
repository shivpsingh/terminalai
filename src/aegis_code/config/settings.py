"""Application settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration loaded from env vars."""

    db_url: str = "sqlite+pysqlite:///aegis.db"
    approval_mode: str = "auto_approve_safe"
    workspace_root: str = "."

    model_config = SettingsConfigDict(env_prefix="AEGIS_", extra="ignore")
