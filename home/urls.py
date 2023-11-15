from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('persons/', views.PersonView.as_view(), name='person_view'),
    path('questions/', views.QuestionListView.as_view()),
    path('questions/create/', views.QuestionCreateView.as_view()),
    path('questions/update/<int:pk>', views.QuestionUpdate.as_view()),
    path('questions/delete/<int:pk>', views.QuestionDeleteView.as_view()),
]
