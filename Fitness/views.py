from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout


from .models import Productz, UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, RegistrationForm
import uuid
from uuid import uuid4

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
    products=Productz.objects.all()
    context={
        'products':products
    }
    return render(request,template_name='Fitness/products.html',context= context)
def cart(request):
    return render(request,template_name='Fitness/cart.html')

def product_details(request,p_id):
    products = Productz.objects.get(pk = p_id)
    context = {
        'product':products
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

def update_product(request,p_id):
   product = Productz.objects.get(pk = p_id)
   form = ProductForm(instance = product)
   if request.method == 'POST':
       form = ProductForm(request.POST, request.FILES,instance = product)
       if form.is_valid():
           form.save()
           return redirect('index')
   context = {'form':form}
   return render(request, template_name = 'Fitness\product_form.html', context= context)

def delete_product(request,p_id):
   product = Productz.objects.get(pk=p_id)
   if request.method == 'POST':
       product.delete()
       return redirect('index')
   return render(request, template_name = 'Fitness\delete_product.html')
def about(request):
    return render(request,template_name='Fitness/about.html')
def member(request):
    return render(request,template_name='Fitness/member.html')
def coaching(request):
    return render(request,template_name='Fitness/coaching.html')
def challenge(request):
    return render(request,template_name='Fitness/challenge.html')
def learnmore(request):
    return render(request,template_name='Fitness/learnmore.html')


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Corrected attribute access for UserProfile
                if hasattr(user, 'userprofile') and user.userprofile.is_admin:
                    return redirect('products')  # Redirect to volunteer dashboard
                else:
                    return redirect('index')  # Redirect to normal user dashboard
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def sign_up(request, user_type):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a UserProfile instance associated with the user
            is_admin = True if user_type == 'Admin' else False
            UserProfile.objects.create(user=user, is_admin=is_admin)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_user(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page after logout

def select_user(request):
    return render(request, 'registration/select_user.html')