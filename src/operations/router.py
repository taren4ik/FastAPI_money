from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.datebase import get_async_session
from src.operations.models import operation
from src.operations.shemas import Operation

router = APIRouter(
    prefix='/operations',
    tags=['Operation']
)


@router.get('/', response_model=List[Operation])
async def get_specific_opertaions(operation_type: str,
                                  session: AsyncSession = Depends(
                                      get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()


@router.post('/')
async def add_specific_opertaions(new_operation: Operation, session:
    AsyncSession = Depends(get_async_session)):
    return {'status': 'succeess'}