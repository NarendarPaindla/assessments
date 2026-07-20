import time
import logging

from fastapi import Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("skillhub")


async def logging_middleware(request: Request, call_next):
    start_time = time.perf_counter()

    request_id = getattr(request.state, "request_id", "N/A")

    logger.info(
        f"[{request_id}] Incoming {request.method} {request.url.path}"
    )

    response = await call_next(request)

    process_time = (time.perf_counter() - start_time) * 1000

    logger.info(
        f"[{request_id}] Response {response.status_code} | {process_time:.2f} ms"
    )

    return response