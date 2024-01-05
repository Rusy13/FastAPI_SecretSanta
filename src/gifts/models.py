from sqlalchemy import ForeignKey, Table, Column, Integer, String, TIMESTAMP, MetaData
from src.auth.models import user
# from src.database import metadata

# metadata = MetaData()


# from sqlalchemy import TIMESTAMP, Column, Integer, String, Table

from src.database import metadata

gift = Table("gift",metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("user_id", Integer, ForeignKey(user.c.id)),

)







