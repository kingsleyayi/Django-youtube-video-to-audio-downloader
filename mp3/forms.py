from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.models import User


class SongForm(ModelForm):
	class Meta:
		model = Song
		fields = '__all__'

class ContactForm(ModelForm):
	message = forms.CharField( widget=forms.Textarea )
	email = forms.EmailField(max_length=200, required=True)
	class Meta:
		model = Messages
		fields = '__all__'