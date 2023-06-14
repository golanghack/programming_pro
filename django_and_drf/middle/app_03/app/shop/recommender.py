import redis
from django.conf import settings
from .models import Product


# connect with redis 
r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

class Recommender:
    """Recommendation system for product to users of shop""" 

    def get_product_key(self, id):
        return f'prouct:{id}:purchased_with'

    def product_bought(self, products):
        product_ids = [p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
                # get another product bought with this product
                if product_id != with_id:
                    # upper count with product
                    r.zincrby(self.get_product_key(product_id), 1, with_id)