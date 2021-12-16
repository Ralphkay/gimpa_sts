from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):

       

       
        class Meta:
             
            model = User
            fields = ['email','username','password','password2']
            choices = (
                    ('100','Level 100'),
                    ('200','Level 200'),
                    ('300','Level 300'),
                    ('400','Level 400'),
                    ('600','Level 600'),
                    ('700','Level 700'),
                )
           

            widgets = {
                'email':forms.TextInput(attrs={'placeholder':'Email'}),
                'username':forms.TextInput(attrs={'placeholder':'Username'}),
                'password':forms.PasswordInput(attrs={'placeholder':'••••••••'}),
                'password2':forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),
                'level':forms.Select(attrs={'placeholder':'Level'}, choices=choices )
            }
