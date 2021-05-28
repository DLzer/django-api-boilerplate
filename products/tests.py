import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Product
# Create your tests here.

class ProductModelTests(TestCase):

    def test_was_published_recently_with_old_product(self):
        """
        was_published_recently() returns False for products whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_product = Product(pub_date=time)
        self.assertIs(old_product.was_published_recently(), False)

    def test_was_published_recently_with_recent_product(self):
        """
        was_published_recently() returns True for products whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_product = Product(pub_date=time)
        self.assertIs(recent_product.was_published_recently(), True)