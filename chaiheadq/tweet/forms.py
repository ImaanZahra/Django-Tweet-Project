from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

    
class TweetForm(forms.ModelForm):
    class Meta:
        #give model and feilds you want to use
        model= Tweet
        fields = ['text', 'photo'] #array

class UserRegisterationForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2') #we are using tuple here because we are using django built in forms
