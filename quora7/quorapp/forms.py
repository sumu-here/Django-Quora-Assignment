from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Question,Answers

class userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Answers_form(forms.ModelForm):
  class Meta:
    model = Answers
    fields =['body']

class Question_form(forms.ModelForm):
    class Meta:
        model=Question
        fields = ['title','body','image']
      
