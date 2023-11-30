from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("register_resident/", views.register_resident, name="register-resident"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("all_residents/", views.all_residents, name="all-residents"),
    path("logout/", LogoutView.as_view(), name="logout"),
]