from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Productz(models.Model):
        objects = None
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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_admin = models.BooleanField(default=True)


class Challenge(models.Model):
    c_id = models.AutoField(primary_key=True)  # Ensure unique ID is auto-generated
    title = models.CharField(max_length=100)
    description = models.TextField()  # Short description for the challenge
    details = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Challenge_image/', blank=True, null=True)

    def __str__(self):
        return self.title

class Trainer(models.Model):
    t_id = models.AutoField(primary_key=True)  # Unique ID for each trainer
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='trainers/')  # Store image in 'trainers/' folder
    bio = models.TextField()  # Detailed bio for the trainer

    def __str__(self):
        return self.name