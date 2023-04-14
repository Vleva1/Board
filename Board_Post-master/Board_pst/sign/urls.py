from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SingupView, LoginView, LoginSignatureView


urlpatterns = [
    path('signup/', SingupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/signature/', LoginSignatureView.as_view(), name='login_signature'),
]









