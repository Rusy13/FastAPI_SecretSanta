from typing import Optional

from fastapi_users import schemas
from pydantic import BaseModel


# class GiftRead(schemas.BaseUser[int]):
#     id: int
#     giftname:str
#     user_id:int


class GiftCreate(BaseModel):
    name: str
    user_id: int
