from datetime import datetime
from sqlalchemy import (Boolean, MetaData, Table, Column, Integer, String,
                        TIMESTAMP, ForeignKey, JSON)

metadate = MetaData()

role = Table(
    'role',
    metadate,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permissions', JSON)
)

user = Table(
    'user',
    metadate,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow()),
    Column('role_id', Integer, ForeignKey('role.c.id'),),
    Column('is_active', Boolean, nullable=False),
    Column('is_superuser', Boolean, nullable=False),
    Column('is_verified', Boolean, nullable=False),

)
