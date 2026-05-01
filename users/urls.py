from django.contrib.auth.views import LoginView
from django.urls import path

from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("registration/", views.UserRegistration.as_view(), name="registration"),
    path("email_validation/<str:token>/", views.token_valid, name="email_validation"),
]
