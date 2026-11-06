-- Runs once, on first container start (empty volume).
-- pgvector powers policy retrieval; pg_trgm helps fuzzy keyword search for hybrid RAG.
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
