from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Productz(models.Model):
        name = models.CharField(max_length=100)
        p_id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False,
        )
        category = models.CharField(max_length=50)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        stock_quantity = models.IntegerField()
        image = models.ImageField(upload_to='product_images/', blank=True, null=True)
        description = models.TextField()
        rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)


        def __str__(self):
            return self.name
