from fastapi import APIRouter

from src.api.handlers.v1 import user, ai

app_routes_v1 = APIRouter(prefix='/v1')

app_routes_v1.include_router(user.router)
app_routes_v1.include_router(ai.router)
