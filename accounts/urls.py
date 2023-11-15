from django.urls import path
from rest_framework.authtoken import views as auth_views
from rest_framework import routers

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('api-auth-token/', auth_views.obtain_auth_token, name='user_token')
]

router = routers.SimpleRouter()
router.register('users', views.UserViewSet)
urlpatterns += router.urls
