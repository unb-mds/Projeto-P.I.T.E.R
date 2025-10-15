from fastapi import APIRouter
import time

router = APIRouter(tags=["infra"])
_START = time.time()

@router.get("/health")
def health():
    return {"status": "ok", "uptime_s": round(time.time() - _START, 2)}
