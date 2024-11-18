from django.shortcuts import render,redirect
from .models import Products
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("Fitness:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})



def login(request):
    return render(request,template_name='registration/login.html')
@login_required
def index(request):
    return render(request,template_name='Fitness/index.html')


def products(request):
    products=Products.objects.all()
    context={
        'products':products
    }
    return render(request,template_name='Fitness/products.html',context= context)
def cart(request):
    return render(request,template_name='Fitness/cart.html')

def product_details(request,id):
    product = Product.objects.get(pk = id)
    context = {
        'product':product,
    }
    return render(request,template_name = 'Fitness/product_details.html',context = context)

