from typing import Any, List
from app.integration.api.clients.querido_diario_client import FilterParams

class PiterApiOrchestrator:
    """
    Orquestrador stub para desenvolvimento.
    Substitua por integrações reais (Querido Diário, NLP etc.).
    """
    async def get_enriched_gazette_data(self, filters: FilterParams) -> List[Any]:
        # Retorno fake só para validar o fluxo
        return [{
            "territory_id": filters.territory_ids,
            "query": filters.querystring,
            "period": [filters.published_since, filters.published_until],
            "size": filters.size,
            "source": "stub"
        }]

