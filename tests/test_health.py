import pytest
from httpx import ASGITransport, AsyncClient

from nimbusgear.api.main import app
from nimbusgear.config import Settings


def test_settings_defaults() -> None:
    s = Settings(_env_file=None)
    assert s.refund_auto_approve_limit == 200
    assert s.triage_model.startswith("claude-")


@pytest.mark.integration
async def test_health_all_services_up() -> None:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.get("/health")
    assert resp.status_code == 200, resp.json()
    assert resp.json() == {"status": "ok", "version": "0.1.0", "postgres": "ok", "redis": "ok"}
