from fastapi import APIRouter

from .modules import include_api_routers

router = APIRouter(prefix="/api")
include_api_routers(router)

