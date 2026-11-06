"""Typed application settings, loaded from environment variables / .env."""

from decimal import Decimal
from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+asyncpg://nimbus:nimbus@localhost:5433/nimbusgear"
    redis_url: str = "redis://localhost:6379/0"

    anthropic_api_key: SecretStr | None = None
    triage_model: str = "claude-haiku-5-5"
    planner_model: str = "claude-sonnet-5-5"

    # Refunds above this amount must go to the human approval queue.
    refund_auto_approve_limit: Decimal = Decimal("200")


@lru_cache
def get_settings() -> Settings:
    return Settings()
