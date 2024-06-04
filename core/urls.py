from django.urls import path
from django.contrib.auth import views as auth_view
from .forms import LoginForm
from . import views
app_name = 'core'
urlpatterns = [
    path('',views.index),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm),name='login'),
    # path('logout/',auth_view.LogoutView.as_view(),name='logout')
]