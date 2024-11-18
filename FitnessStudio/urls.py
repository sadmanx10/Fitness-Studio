"""
URL configuration for FitnessStudio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Fitness import views as f_views
from . import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',f_views.index,name='index'),
    #path('login.html',f_views.login,name='login'),
    path('products.html',f_views.products,name='products'),
    path('/<str:id>', f_views.product_details, name='product_details'),
    path('cart.html',f_views.cart,name='cart'),
    path('login.html', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', f_views.authView, name="authView"),
    path("", include(("Fitness.urls", "Fitness"), "Fitness"))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
