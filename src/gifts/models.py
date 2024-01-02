from sqlalchemy import ForeignKey, Table, Column, Integer, String, TIMESTAMP, MetaData
from src.auth.models import users
metadata = MetaData()

gift = Table("gift",metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("user_id", Integer, ForeignKey(users.c.id)),

)
