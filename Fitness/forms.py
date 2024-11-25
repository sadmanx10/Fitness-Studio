from django.forms import ModelForm
from .models import *



class ProductForm(ModelForm):
   class Meta:
       model = Productz
       fields = '__all__'