from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.gifts.models import gift
from src.gifts.schemas import GiftCreate

router = APIRouter(
    prefix="/gifts",
    tags=["Gifts"]
)




# @router.get("/")
# async def get_specific_operations(gift_name: str, session: AsyncSession = Depends(get_async_session)):
#     query = select(gift).where(gift.c.name == gift_name)
#     result = await session.execute(query)
#     return result.all()

@router.get("/")
async def get_specific_operations(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(gift).where(gift.c.user_id == user_id)
    result = await session.execute(query)

    # Получение имен столбцов из результата запроса
    columns = result.keys()

    # Создание списка словарей на основе значений строк
    gift_data = [dict(zip(columns, row)) for row in result.all()]

    ans = [item["name"] for item in gift_data]

    return ans




@router.post("/")
async def add_gifts(new_gift: GiftCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(gift).values(**new_gift.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
