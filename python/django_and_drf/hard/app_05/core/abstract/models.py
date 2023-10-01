from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class AbstractManager(models.Manager):
    """Create abstract manager from base manager from model class"""
    
    def get_object_by_public_id(self, public_id: int):
        """Return instance or Http404""" 

        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

class AbstractModel(models.Model):
    public_id = models.UUIDField(
        db_index=True, 
        unique=True, 
        default=uuid.uuid4,
        editable=False 
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = AbstractManager()

    class Meta:
        abstract = True

    def save(
        self, 
        force_insert=False, 
        force_update=False, 
        using=None, 
        update_fields=None
    ):
        return super(AbstractModel, self).save(
            force_insert=force_insert, 
            force_update=force_update, 
            using=using, 
            update_fields=update_fields,
            )

    def delete(self, 
        using=None, 
        keep_parents=False):
        return super(AbstractModel, self).delete(
            using=using, 
            keep_parents=keep_parents
        )

    