from django import forms
from .models import Address

#Django Forms
class NewOwnerForm(forms.Form):
    f_name=forms.CharField(label="First Name",max_length=20,required=True)
    l_name=forms.CharField(label="Last Name",max_length=20,required=True)
    mobile=forms.IntegerField(label="Mobile Numer",required=True,min_value=7000000000,max_value=9000000000,error_messages={'required':"please enter a valid mobile number",'min_value':"Minimum value is 7000000000"})
    email=forms.EmailField(label="Email",max_length=30,required=True,error_messages={'required':"This is a mandatory filed pleease filled it",'max_lenght':'The email must not be more than 50 characters'})

#Model Forms
class NewAdreessModelForm(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'