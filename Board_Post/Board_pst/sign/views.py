from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import LoginForm, SignatureForm
from .models import PrivacySignature


class SingupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'signup.html'


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            target = redirect('/board')
        else:
            new_privacy_signature = PrivacySignature.new_privacy_signature(user=user)
            send_mail(
                subject='Login to Board-Post',
                message=f'Privacy signature: {new_privacy_signature}',
                from_email='',
                recipient_list=[user.email],
                fail_silently=False,
            )
            target = redirect(f'signature/?username={username}')
        return target


class LoginSignatureView(FormView):
    form_class = SignatureForm
    template_name = 'login_signature.html'

    def post(self, request, *args, **kwargs):
        signature = request.POST['signature']
        user = User.objects.get(username=request.GET.get('username'))
        verify_signature = str(PrivacySignature.get_privacy_signature(user))
        if signature == verify_signature:
            login(request=request, user=user)
        return redirect('/board')





















