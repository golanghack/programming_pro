from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import uuid

class AbstractManager(models.Manager):
    """Abstract manager class for models""" 

    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

class AbstractModel(models.Model):
    """Abstract model -> DRY princip""" 

    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True