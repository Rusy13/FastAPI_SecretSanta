# import smtplib
# from email.message import EmailMessage

# from celery import Celery

# from src.config import SMTP_PASSWORD, SMTP_USER
# from src.gifts.router import get_specific_operations

# SMTP_HOST = "smtp.gmail.com"
# SMTP_PORT = 465

# celery = Celery('tasks', broker='redis://localhost:6379')


# def get_email_template_dashboard(username: str, user_id:int, ans:list):
#     email = EmailMessage()
#     email['Subject'] = 'Подарки'
#     email['From'] = SMTP_USER
#     email['To'] = SMTP_USER


#     email.set_content(
#         '<div>'
#         f'<h1 style="color: red;">Здравствуйте! Ваш список подарков:</h1>' #{ans}</h1>'
#         '</div>',
#         subtype='html'
#     )
#     return email


# @celery.task
# def send_email_report_dashboard(username: str, user_id: int, ans:list):
#     email = get_email_template_dashboard(username, user_id, ans)
#     with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
#         server.login(SMTP_USER, SMTP_PASSWORD)
#         server.send_message(email)


























import smtplib
from email.message import EmailMessage

from celery import Celery

from src.config import SMTP_PASSWORD, SMTP_USER

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')


def get_email_template_dashboard():
    email = EmailMessage()
    email['Subject'] = 'Натрейдил Отчет Дашборд'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Ваши подарки - .</h1>'
        '</div>',
        subtype='html'
    )
    return email


@celery.task
def send_email_report_dashboard():
    # email = get_email_template_dashboard()
    # with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
    #     server.login(SMTP_USER, SMTP_PASSWORD)
    #     server.send_message(email)
    print('log')