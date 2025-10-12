from django.contrib import admin
from django.urls import path, include   

from Fitness import views as f_views
from . import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', f_views.index, name='index'),

    #Add this for Google Login
    path('accounts/', include('allauth.urls')),

    path('login.html/', f_views.login_page, name='login'),
    path('signup/<str:user_type>/', f_views.sign_up, name='signup'),
    path('select_user/', f_views.select_user, name='select_user'),
    path('logout/', f_views.logout_user, name='logout'),
    path('products/', f_views.products, name='products'),
    path('about/', f_views.about, name='about'),
    path('member/', f_views.member, name='member'),
    path('trainers/', f_views.trainers_list, name='trainers_list'),
    path('trainer/<int:t_id>/', f_views.trainer_detail, name='trainer_detail'),
    path('add_trainer/', f_views.add_trainer, name='add_trainer'),
    path('delete_trainer/<int:t_id>/', f_views.delete_trainer, name='delete_trainer'),
    path('profile/', f_views.profile_view, name='user_profile'),
    path('challenge/', f_views.challenges, name='challenge'),
    path('challenge/create/', f_views.create_challenge, name='create_challenge'),
    path('update_challenge/<str:c_id>', f_views.update_challenge, name='update_challenge'),
    path('delete_challenge/<str:c_id>', f_views.delete_challenge, name='delete_challenge'),
    path('learnmore.html', f_views.learnmore, name='learnmore'),
    path('add-to-cart/<uuid:product_id>/', f_views.add_to_cart, name='add_to_cart'),
    path('cart/', f_views.view_cart, name='view_cart'),
    path('cart/increase/<uuid:product_id>/', f_views.increase_cart_quantity, name='increase_cart_quantity'),
    path('cart/decrease/<uuid:product_id>/', f_views.decrease_cart_quantity, name='decrease_cart_quantity'),
    path('remove-from-cart/<uuid:product_id>/', f_views.remove_from_cart, name='remove_from_cart'),
    path('upload_product/', f_views.upload_product, name='upload_product'),
    path('update_product/<str:p_id>', f_views.update_product, name='update_product'),
    path('delete_product/<str:p_id>', f_views.delete_product, name='delete_product'),

    # Session URLs
    path('sessions/', f_views.session_list, name='sessions'),
    path('sessions/create/', f_views.create_session, name='create_session'),
    path('sessions/<int:session_id>/edit/', f_views.edit_session, name='edit_session'),
    path('sessions/<int:session_id>/delete/', f_views.delete_session, name='delete_session'),

    # 🔻 These MUST be at the bottom
    path('<str:c_id>/', f_views.challenge_detail, name='challenge_detail'),
    path('<str:p_id>', f_views.product_details, name='product_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
