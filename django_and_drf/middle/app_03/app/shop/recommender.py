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

    def suggest_products_for(self, products, max_results=6):
        product_ids = [p.id for p in products]
        if len(products) == 1:
            # only one 
            suggestions = r.zrange(self.get_product_key(product_ids[0]),
                            0, -1, desc=True)[:max_results]
        else:
            # generated short-time key
            flat_ids = ''.join([str(id) for id in product_ids])
            tmp_key = f'tmp {flat_ids}'
            # someone products union all products
            # save getting sorted set
            # in short-time key
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(tmp_key, keys)
            # remove ids products with recommended
            r.zrem(tmp_key, *product_ids)
            # get ids product for count
            # sorting -> from large to small
            suggestions = r.zrange(tmp_key, 0, -1, desc=True)[:max_results]
            # remove short-time key
            r.delete(tmp_key)
        suggested_products_ids = [int(id) for id in suggestions]
        # get products suggests and sorted for order to exist
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))
        return suggested_products
    
    def clear_purchases(self):
        for id in Product.objects.values_list('id', flat=True):
            r.delete(self.get_product_key(id))