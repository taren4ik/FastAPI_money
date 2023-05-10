from typing import List

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette import status

from auth.datebase import User
from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.shemas import UserCreate, UserRead

from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers


app = FastAPI(
    title='Money App'
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
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

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def unprotected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected-route")
def protected_route():
    return f"Hello, anonimus"

# fake_users = [
#     {'id': 1, 'role': 'admin', 'name': ['Bob']},
#     {'id': 2, 'role': 'investor', 'name': 'John'},
#     {'id': 3, 'role': 'trader', 'name': 'Matt'},
#     {'id': 4,
#      'role': 'trader',
#      'name': 'Matt',
#      'degree': [{'id': 1,
#     'created_date': '2020-01-01T00:00:00',
#     'type_degree': 'expert'
# }]},
# ]
#
#
# @app.get('/users/{user_id}/', response_model=List[User])
# def get_user(user_id: int):
#     return [user for user in fake_users if user_id == user.get('id')]
#
#
# fake_trades = [
#     {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123,
#      'amount': 2.12},
#     {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123,
#      'amount': 2.12}
# ]
#
#
# @app.get('/trades')
# def get_trades(limit: int = 1, offset: int = 0):
#     return fake_trades[offset:][:limit]
#
#
# fake_users2 = [
#     {'id': 1, 'role': 'admin', 'name': 'Bob'},
#     {'id': 2, 'role': 'investor', 'name': 'John'},
#     {'id': 3, 'role': 'trader', 'name': 'Matt'}
# ]
#
#
# @app.post('/trades')
# def add_trades(trades: List[Trade]):
#     fake_trades.extend(trades)
#     return {'status': 200, 'data': fake_trades}
