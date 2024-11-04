from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    return render(request,template_name='Fitness/index.html')

def login(request):
    return render(request,template_name='Fitness/login.html')
def products(request):
    products=Products.objects.all()
    context={
        'products':products
    }
    return render(request,template_name='Fitness/products.html')
def cart(request):
    return render(request,template_name='Fitness/cart.html')

