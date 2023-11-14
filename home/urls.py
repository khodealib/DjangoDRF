from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('persons/', views.PersonView.as_view(), name='person_view'),
]
