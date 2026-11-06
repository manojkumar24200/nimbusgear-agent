# NimbusGear Support Resolution Agent

An AI agent that **resolves** customer support tickets for NimbusGear, a fictional online electronics store. It doesn't just answer questions. It looks up the order, checks the policy, takes the action (refund, reship, address change), hands off to a human when it should, and measures how well all of that works.

> Status: **Phase 0: foundations.** Metrics will appear here once the eval harness lands.

## Stack

LangGraph · FastAPI · Postgres + pgvector · Redis · Claude (Haiku for triage, Sonnet for planning) · HTMX dashboard · Docker · GitHub Actions

## Quickstart

```bash
cp .env.example .env          # add ANTHROPIC_API_KEY (needed from Phase 2)
docker compose up -d          # Postgres (pgvector) + Redis
uv sync                       # install dependencies
uv run pytest                 # unit + integration tests
uv run uvicorn nimbusgear.api.main:app --reload
# → http://localhost:8000/health   and   http://localhost:8000/docs
```

## Roadmap

| Phase | Scope | Status |
|---|---|---|
| 0 | Foundations: repo, Docker, config, CI | ✅ |
| 1 | The world: schema, synthetic data, policy docs, mock Orders/Payments API | ⏳ |
| 2 | Single-agent MVP: triage, typed tools, policy RAG, LangGraph flow | |
| 3 | Eval harness: golden set, outcome and trajectory checks, scorecard | |
| 4 | Safety and HITL: guardrails, permissions, idempotency, approval interrupt/resume | |
| 5 | Multi-agent: router + specialists, compared with single-agent in evals | |
| 6 | Production polish: hybrid RAG + reranker, memory, observability, cost routing, dashboard, MCP | |
| 7 | Ship: 250-case eval suite, CI regression gate, Fly.io deploy | |
