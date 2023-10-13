from celery import shared_task
from django.core.mail import EmailMessage

@shared_task
def send_shipment_email(owner_name: str, order_name: str, owner_email: str):
    mail_subj = 'Ваш заказ готов'
    message = f'Здравствуйте {owner_name}, ваш заказ {order_name} готов к отправке'
    email = EmailMessage(mail_subj, message, to=[owner_email])
    email.send()