from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.core.logging import logger

# 👉 Ajuste os imports para apontarem para dentro do pacote `app/`
#    (mova suas pastas para app/services/... conforme a nova estrutura)
from app.services.integration.piter_api_orchestrator import PiterApiOrchestrator
from app.services.api.clients.querido_diario_client import FilterParams

import time

app = FastAPI(
    title=settings.APP_NAME,
    description="Plataforma de Integração e Transparência em Educação e Recursos",
    version=settings.APP_VERSION,
)

# CORS (lido a partir de .env via settings)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.CORS_ORIGINS.split(",") if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Booting API…")
orchestrator = PiterApiOrchestrator()
_START = time.time()

@app.get("/")
async def read_root():
    return {
        "project": "P.I.T.E.R",
        "status": "Online",
        "description": "API para consulta de diários oficiais municipais",
        "version": settings.APP_VERSION,
    }

# Health padronizado (com uptime)
@app.get("/health", tags=["infra"])
async def health_check():
    return {"status": "ok", "uptime_s": round(time.time() - _START, 2)}

@app.get("/api/v1/gazettes")
async def get_gazettes(
    territory_ids: str = Query(..., description="Código IBGE do município"),
    published_since: str | None = Query(None, description="Data inicial (YYYY-MM-DD)"),
    published_until: str | None = Query(None, description="Data final (YYYY-MM-DD)"),
    querystring: str | None = Query(None, description="Palavra-chave para busca"),
    size: int = Query(5, description="Quantidade de resultados", ge=1, le=100),
):
    """
    Endpoint principal para buscar e enriquecer diários oficiais.
    Retorna dados do Querido Diário com possível análise NLP.
    """
    try:
        filters = FilterParams(
            territory_ids=territory_ids,
            published_since=published_since,
            published_until=published_until,
            querystring=querystring,
            size=size,
        )
        enriched_gazettes = await orchestrator.get_enriched_gazette_data(filters)
        return enriched_gazettes
    except Exception as e:
        logger.exception("Erro no /api/v1/gazettes")
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}") from e
