from django.urls import path
#from . import views
from .views import SignUpView
from django.contrib.auth import views as authorization_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password_change/', authorization_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),),
    path('password_reset/', authorization_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),),
]
