from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@shared_task
def payment_completed(order_id):
    """Task for send push email about paid an order"""

    order = Order.objects.get(id=order_id)
    # create email
    subject = f"ZoechkaMag -> заказ номер {order.id}"
    message = "Пожалуйста, ознакомьтесь с вашим заказом"
    email = EmailMessage(subject, message, "admin@shop.com", [order.email])

    # pdf
    html = render_to_string("orders/order/pdf.html", {"order": order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / "css/pdf.css")]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # glue pdf
    email.attach(f"order_{order.id}.pdf", out.getvalue(), "application/pdf")

    # send
    email.send()
