from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from .models import *


class ContactForm(forms.ModelForm):
    class Meta: 
        model = Contact 
        fields = ['name','phone','email','title','message','ip'] 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CustomerForm(forms.ModelForm):
    class Meta: 
        model = Customer 
        fields = ['phone','address'] 
        
class ComplaintForm(forms.ModelForm):
    class Meta: 
        model = Complaint 
        fields = ['title','message', 'image','status'] 
    
class InternetPlansForm(forms.ModelForm):
    class Meta: 
        model = InternetPlans 
        fields = ['speed','price','validity','message'] 

class FaqForm(forms.ModelForm):
    class Meta: 
        model =  Faq
        fields = ['title','solution'] 