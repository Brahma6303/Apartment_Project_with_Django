from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
# Create your views here.

class NewRegistationPageView(CreateView):
    template_name='users/register.html'
    form_class=UserRegistrationForm
    success_url='/users/login'
    #success_url=reverse_lazy('users:login')