from django.urls import path
from rest_framework.authtoken import views as auth_views

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('api-auth-token/', auth_views.obtain_auth_token, name='user_token')
]
