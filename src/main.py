from src.auth.models import User
from src.auth.base_config import auth_backend, fastapi_users
from src.auth.shemas import UserCreate, UserRead

from fastapi import FastAPI, Depends
from src.operations.router import router as router_operation
from fastapi_users import FastAPIUsers


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
