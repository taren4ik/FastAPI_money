from src.auth.models import User
from src.auth.base_config import auth_backend, fastapi_users
from src.auth.shemas import UserCreate, UserRead

from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers


app = FastAPI(
    title='Money App'
)

# fastapi_users = FastAPIUsers[User, int](
#     get_user_manager,
#     [auth_backend],
# )

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

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def unprotected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def protected_route():
    return f"Hello, anonimus"
