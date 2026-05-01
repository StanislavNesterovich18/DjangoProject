import secrets

from django.contrib.auth import logout
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import CustomUserCreationForm
from users.models import User


def logout_view(request):
    logout(request)
    return redirect(reverse("catalog:home"))


class UserRegistration(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.token =secrets.token_hex(16)
        user.save()
        #Отправка на почту
        host = self.request.get_host()
        url = f"http://{host}/user/email_validation/{user.token}/"
        send_mail(subject="Email Validation",
                  message=f"Подтвердите почту, перейдя по ссылке: {url}",
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email])
        return super(UserRegistration, self).form_valid(form)

def token_valid(request, token):
    user = User.objects.filter(token=token)
    if user.exists():
        user=user[0]
        user.is_active = True
        user.save()
    return redirect(reverse("catalog:home"))



