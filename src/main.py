from src.auth.models import User
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend


from src.auth.base_config import auth_backend, fastapi_users
from src.auth.shemas import UserCreate, UserRead

from fastapi import FastAPI, Depends
from src.operations.router import router as router_operation
from src.tasks.router import router as router_tasks
from redis import asyncio as aioredis

app = FastAPI(
    title='Money App'
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(router_operation)
app.include_router(router_tasks)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
