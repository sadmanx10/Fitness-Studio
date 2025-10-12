from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout


from .models import Productz, UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, RegistrationForm,ChallengeForm,TrainerForm
from .models import UserProfile,Challenge,Trainer
import uuid
from uuid import uuid4
from .models import Productz


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
# def coaching(request):
#     return render(request,template_name='Fitness/trainers_list.html')
def challenges(request):
    challenges = Challenge.objects.all()
    context = {
        'challenge': challenges
    }
    return render(request, template_name='Fitness/challenge.html', context= context)

def challenge_detail(request, c_id):
    challenge = get_object_or_404(Challenge, pk=c_id)
    context = {
        'challenge': challenge
    }
    return render(request, template_name='Fitness/challenge_detail.html',  context= context)
def create_challenge(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('challenge')  # Redirect to the challenges list after saving
    else:
        form = ChallengeForm()
    context = {'form': form}
    return render(request, template_name='Fitness/create_challenge.html', context= context)


def update_challenge(request, c_id):
    challenge = get_object_or_404(Challenge, pk=c_id)
    if request.method == 'POST':
        form = ChallengeForm(request.POST, request.FILES, instance=challenge)
        if form.is_valid():
            form.save()
            return redirect('challenge')  # Replace with the name of your challenge list view
    else:
        form = ChallengeForm(instance=challenge)
    return render(request, 'Fitness/update_challenge.html', {'form': form, 'challenge': challenge})

def delete_challenge(request, c_id):
    challenge = get_object_or_404(Challenge, pk=c_id)
    if request.method == 'POST':
        challenge.delete()
        return redirect('challenge')  # Replace with the name of your challenge list view
    return render(request, 'Fitness/delete_challenge.html', {'challenge': challenge})

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
def profile_view(request):
    # Assuming the logged-in user is viewing their own profile
    user_profile = get_object_or_404(UserProfile, user=request.user)

    return render(request, 'registration/profile.html', {'user_profile': user_profile})

def trainers_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'Fitness/trainers_list.html', {'trainers': trainers})

# View trainer details
def trainer_detail(request, t_id):
    trainer = get_object_or_404(Trainer, pk=t_id)
    return render(request, 'Fitness/trainer_detail.html', {'trainer': trainer})

# Add a new trainer
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainers_list')
    else:
        form = TrainerForm()
    return render(request, 'Fitness/add_trainer.html', {'form': form})

# Delete a trainer
def delete_trainer(request, t_id):
    trainer = get_object_or_404(Trainer, pk=t_id)
    if request.method == 'POST':
        trainer.delete()
        return redirect('trainers_list')
    return render(request, 'Fitness/delete_trainer.html', {'trainer': trainer})


def add_to_cart(request, product_id):
    product = get_object_or_404(Productz, p_id=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')

def increase_cart_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
        request.session['cart'] = cart
    return redirect('view_cart')

def decrease_cart_quantity(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart and cart[str(product_id)] > 1:
        cart[str(product_id)] -= 1
        request.session['cart'] = cart
    elif str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Productz, p_id=product_id)
        total += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity,
        })

    return render(request, 'Fitness/cart.html', {'cart_items': cart_items, 'total': total})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart  # Save the updated cart back to session

    return redirect('view_cart')

