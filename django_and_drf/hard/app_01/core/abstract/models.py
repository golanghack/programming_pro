from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class AbstractManager(models.Manager):
    """-> Create absnhact manager model"""

    def get_object_by_public_id(self, public_id):
        """-> get object from public id orientation"""

        try: 
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

class AbstractModel(models.Model):
    """-> abstract model"""

    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = AbstractManager()

    class Meta:
        abstract = True

