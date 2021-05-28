import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(default=None, blank=True, null=True, max_length=200)
    pub_date     = models.DateTimeField('date published')

    def __str__(self):
        return self.product_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now