from django.urls import path
from account import views


urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.profile, name="profile"),
    path("change_password", views.change_password, name="change_password"),
]
