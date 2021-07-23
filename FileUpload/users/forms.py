from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["first_name","last_name",'username','email']




		# widgets = {

		# 'first_name' : forms.TextInput(attrs = {'class':'mt-5'})
		# }