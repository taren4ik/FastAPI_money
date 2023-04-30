import datetime
from typing import List, Optional

from pydantic import BaseModel, Field
from enum import Enum


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


class Degree(BaseModel):
    id: int
    created_date: datetime.datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]] = []
