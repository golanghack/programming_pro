from django.test import TestCase
from coupons.models import Coupon


class TestCouponModel(TestCase):
    """-> coupons test"""

    def test_max_len_code(self):
        """-> test max lenght of code(<= 50)"""

        coupon = Coupon.objects.create()
        coupon_code = coupon
        max_lenght_code = coupon_code._meta.get_field("code").max_length
        len_code = len(coupon_code.code)
        self.assertNotEqual(max_lenght_code, len_code)
        print(coupon_code)
