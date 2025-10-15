from typing import Optional
from dataclasses import dataclass

@dataclass
class FilterParams:
    territory_ids: str
    published_since: Optional[str] = None  # YYYY-MM-DD
    published_until: Optional[str] = None  # YYYY-MM-DD
    querystring: Optional[str] = None
    size: int = 5
