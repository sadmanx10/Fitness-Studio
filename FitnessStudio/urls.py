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
    path('login.html/',f_views.login_page,name='login'),
    #path('logout.html/',f_views.logout,name='logout'),
    path('signup/<str:user_type>/', f_views.sign_up, name='signup'),
    path('select_user/', f_views.select_user, name='select_user'),
    path('logout/',f_views.logout_user, name='logout'),
    path('products.html',f_views.products,name='products'),
    path('about.html',f_views.about,name='about'),
    path('member.html',f_views.member,name='member'),
    path('coaching.html',f_views.coaching,name='coaching'),
    path('challenge.html',f_views.challenge,name='challenge'),
    path('learnmore.html', f_views.learnmore, name='learnmore'),
    path('<str:p_id>', f_views.product_details, name='product_details'),
    #path('profile/', f_views.profile_view, name='profile'),
    path('profile/', f_views.profile_view, name='user_profile'),
    #path('update_product/<str:p_id>', f_views.update_product, name='update_product'),
    path('cart.html',f_views.cart,name='cart'),
    #path('login.html', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('signup/', f_views.authView, name="authView"),
    path("", include(("Fitness.urls", "Fitness"), "Fitness")),
    path('upload_product/', f_views.upload_product, name='upload_product'),
    #path('delete_product/<str:p_id>',f_views.delete_product,name = 'delete_product'),
    path('update_product/<str:p_id>', f_views.update_product, name='update_product'),
    path('delete_product/<str:p_id>', f_views.delete_product, name='delete_product'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
