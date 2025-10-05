from django.contrib import admin
from .models import Productz, Challenge, UserProfile, Trainer

# Register your models here.
admin.site.register([Productz, Challenge, UserProfile, Trainer])
