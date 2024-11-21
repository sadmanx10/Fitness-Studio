from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})




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

def upload_product(request):
   form = ProductForm()
   if request.method == 'POST':
       form = ProductForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('index')
   context = {'form':form}
   return render(request, template_name = 'Fitness\product_form.html', context= context)

def update_product(request,id):
   product = Product.objects.get(pk = id)
   form = ProductForm(instance = product)
   if request.method == 'POST':
       form = ProductForm(request.POST, request.FILES,instance = product)
       if form.is_valid():
           form.save()
           return redirect('home')
   context = {'form':form}
   return render(request, template_name = 'Fitness\product_form.html', context= context)
def about(request):
    return render(request,template_name='Fitness/about.html')
def member(request):
    return render(request,template_name='Fitness/member.html')