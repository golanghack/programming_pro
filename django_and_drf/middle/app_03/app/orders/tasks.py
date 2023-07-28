from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id: int) -> tuple:
    """Task for send push email for successfully order created"""

    order = Order.objects.get(id=order_id)
    subject = f"Заказ номер {order.id}"
    message = (
        f"Уважаемый {order.first_name}, \n\n"
        f"Ваш заказ успешно создан."
        f"ID вашего заказа {order.id}."
    )
    mail_sent = send_mail(subject, message, "admin@admin.com", [order.email])

    return mail_sent
