from django import forms
from .models import CustomUser,UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    #username=forms.CharField(required=True,max_length=30,label='Username*')
    first_name=forms.CharField(required=True,max_length=30,label='First Name*')
    last_name=forms.CharField(required=True,max_length=30,label='Last Name*')
    email=forms.EmailField(required=True,max_length=30,label='Email*')
    age=forms.IntegerField(required=True,max_value=100,label='Age*')
    mobile_number=forms.CharField(required=True,max_length=10,label='Mobile Number*')
    city=forms.CharField(required=True,max_length=30,label='City*')
    country=forms.CharField(required=True,max_length=30,label='Country*')
    
    
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','age','mobile_number','email','city','country']
        widgets={'password':forms.PasswordInput()}

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Username already exists")
        return email
    
    def save(self):
        user =super().save(commit=False)
        user.save()
        profile=UserProfile(age=self.cleaned_data['age'],
                            mobile_number=self.cleaned_data['mobile_number'],
                            city=self.cleaned_data['city'],
                            country=self.cleaned_data['country'],
                            user=user)
        profile.save()
        return user
        
        
        