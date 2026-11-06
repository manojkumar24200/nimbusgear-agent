"""FastAPI entrypoint. Phase 0: health checks only."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from redis.asyncio import Redis

from nimbusgear import __version__
from nimbusgear.config import get_settings
from nimbusgear.db import check_db

app = FastAPI(title="NimbusGear Support Agent", version=__version__)


async def check_redis() -> bool:
    client = Redis.from_url(get_settings().redis_url)
    try:
        return bool(await client.ping())
    finally:
        await client.aclose()


@app.get("/health")
async def health() -> JSONResponse:
    checks: dict[str, str] = {}
    for name, check in (("postgres", check_db), ("redis", check_redis)):
        try:
            await check()
            checks[name] = "ok"
        except Exception as exc:  # report, don't crash, so the endpoint shows what's down
            checks[name] = f"error: {type(exc).__name__}"
    healthy = all(v == "ok" for v in checks.values())
    return JSONResponse(
        status_code=200 if healthy else 503,
        content={"status": "ok" if healthy else "degraded", "version": __version__, **checks},
    )
