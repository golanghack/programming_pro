from django.db import models

from django.contrib.auth.models import AbstractUser

class AdvUser(AbstractUser):
    """AdvUser 
    is_activated -> user is activated?
    send_messages -> user send messages?
    """ 

    is_activeted = models.BooleanField(default=True,
                                    db_index=True, 
                                    verbose_name='Активирован?')
    send_messages = models.BooleanField(default=True,
                                    verbose_name='Отправльять сообщения о комментариях?')
    
    class Meta(AbstractUser.Meta):
        pass
