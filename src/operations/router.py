import time
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from fastapi_cache.decorator import cache
from src.datebase import get_async_session
from src.operations.models import operation
from src.operations.shemas import Operation

router = APIRouter(
    prefix='/operations',
    tags=['Operation']
)


@router.get("/long_operation") #кэширую в течение 30 сек
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись"


@router.get('/', response_model=List[Operation])
async def get_specific_opertaions(operation_type: str,
                                  session: AsyncSession = Depends(
                                      get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "200",
            "data": result.all(),
            "details": None
        }

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None})


@router.post('/')
async def add_specific_opertaions(new_operation: Operation, session:
AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()  # исполнение транзакции
    return {'status': 'succeess'}
