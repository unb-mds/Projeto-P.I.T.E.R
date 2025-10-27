from typing import Any, List, Optional
from datetime import date

# Adapter que permite que a camada `app` (FastAPI) use o orquestrador já
# implementado na pasta `services` sem duplicar lógica.
from app.integration.api.clients.querido_diario_client import FilterParams as AppFilterParams
from services.integration.piter_api_orchestrator import PiterApiOrchestrator as ServicesPiterOrchestrator
from services.api.clients.querido_diario_client import FilterParams as ServicesFilterParams


class PiterApiOrchestrator:
    """Adapter para expor a função `get_enriched_gazette_data` esperada
    pela API (arquivo `app/main.py`) usando a implementação em
    `services.integration.piter_api_orchestrator`.
    """

    def __init__(self):
        self._services = ServicesPiterOrchestrator()

    @staticmethod
    def _parse_date(value: Optional[str]) -> Optional[date]:
        if not value:
            return None
        try:
            return date.fromisoformat(value)
        except Exception:
            # Se falhar no parse, retornamos None e deixamos o cliente lidar com valores inválidos
            return None

    async def get_enriched_gazette_data(self, filters: AppFilterParams) -> List[Any]:
        """Converte App FilterParams para o modelo esperado pelo services
        e repassa a chamada para o orquestrador funcional.
        """
        services_filters = ServicesFilterParams(
            territory_ids=filters.territory_ids or None,
            published_since=self._parse_date(filters.published_since),
            published_until=self._parse_date(filters.published_until),
            querystring=filters.querystring,
            size=filters.size,
        )

        result = await self._services.get_enriched_gazette_data(services_filters)
        return result

