from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, MetaData

from src.database import Base

metadata = MetaData()

department = Table(
    "department",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

users = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("department_id", Integer, ForeignKey(department.c.id)),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)





class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)    
    username = Column( String, nullable=False)
    hashed_password = Column( String, nullable=False)
    registered_at = Column( TIMESTAMP, default=datetime.utcnow)
    department_id = Column( Integer, ForeignKey(department.c.id))
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)


        