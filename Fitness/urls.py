from django.urls import path, include
from .views import authView, index, trainers_list, trainer_detail, add_trainer, delete_trainer

urlpatterns = [
 path("", index, name="index"),
 path("signup.html/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
	path("trainers/", trainers_list, name="trainers_list"),
	path("trainers/<int:t_id>/", trainer_detail, name="trainer_detail"),
	path("trainers/add/", add_trainer, name="add_trainer"),
	path("trainers/<int:t_id>/delete/", delete_trainer, name="delete_trainer"),
]