from django.urls import path, include
from .views import (
    authView, index, trainers_list, trainer_detail, add_trainer, delete_trainer,
    increase_cart_quantity, decrease_cart_quantity, session_list, create_session,
    edit_session, delete_session
)

urlpatterns = [
 path("", index, name="index"),
 path("signup.html/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
	path("trainers/", trainers_list, name="trainers_list"),
	path("trainers/<int:t_id>/", trainer_detail, name="trainer_detail"),
	path("trainers/add/", add_trainer, name="add_trainer"),
	path("trainers/<int:t_id>/delete/", delete_trainer, name="delete_trainer"),
    path("cart/increase/<int:product_id>/", increase_cart_quantity, name="increase_cart_quantity"),
    path("cart/decrease/<int:product_id>/", decrease_cart_quantity, name="decrease_cart_quantity"),
    
    # Session URLs
    path("sessions/", session_list, name="sessions"),
    path("sessions/create/", create_session, name="create_session"),
    path("sessions/<int:session_id>/edit/", edit_session, name="edit_session"),
    path("sessions/<int:session_id>/delete/", delete_session, name="delete_session"),
]