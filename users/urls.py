from django.urls import path 
from . import views

urlpatterns = [
    
    path('register/',views.NewRegistationPageView.as_view()),
    path('login/',views.NewRegistationPageView.as_view()),
    
]
