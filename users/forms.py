from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    #username=forms.CharField(required=True,max_length=30,label='Username*')
    first_name=forms.CharField(required=True,max_length=30,label='First Name*')
    last_name=forms.CharField(required=True,max_length=30,label='Last Name*')
    email=forms.EmailField(required=True,max_length=30,label='Email*')
    
    
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','email']
        widgets={'password':forms.PasswordInput()}

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Username already exists")
        return email
    
    def save(self):
        user =super().save(commit=False)
        user.save()
        return user
        
        
        