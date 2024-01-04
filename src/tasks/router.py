# from fastapi import APIRouter, BackgroundTasks, Depends
# from sqlalchemy import select, insert
# from sqlalchemy.ext.asyncio import AsyncSession

# from src.database import get_async_session

# from src.auth.base_config import current_user
# from src.gifts.router import get_specific_operations

# from src.database import get_async_session
# from src.gifts.models import gift
# from src.gifts.schemas import GiftCreate

# from .tasks import get_email_template_dashboard, send_email_report_dashboard

# router = APIRouter(prefix="/report")



# @router.get("/dashboard")
# async def get_dashboard_report(user_id: int, user_name:str, session: AsyncSession = Depends(get_async_session)):

#     query = select(gift).where(gift.c.user_id == user_id)
#     result = await session.execute(query)

#     # Получение имен столбцов из результата запроса
#     columns = result.keys()

#     # Создание списка словарей на основе значений строк
#     gift_data = [dict(zip(columns, row)) for row in result.all()]

#     ans = [item["name"] for item in gift_data]

#     send_email_report_dashboard.delay(user_name, user_id, ans)
    
#     return {
#         "status": 200,
#         "data": "Письмо отправлено",
#         "details": None
#     }




















from fastapi import APIRouter, BackgroundTasks, Depends

from src.auth.base_config import current_user

from .tasks import send_email_report_dashboard

router = APIRouter(prefix="/report")


@router.get("/dashboard")
# def get_dashboard_report():
def get_dashboard_report():

    # 1400 ms - Клиент ждет
    # send_email_report_dashboard(user.username)
    # 500 ms - Задача выполняется на фоне FastAPI в event loop'е или в другом треде
    # background_tasks.add_task(send_email_report_dashboard, user)
    # 600 ms - Задача выполняется воркером Celery в отдельном процессе
    send_email_report_dashboard.delay()
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }