from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email', 'password1', 'password2']
		widgets = {
		'username':forms.TextInput(attrs ={
			'class': 'input--style-4',
			'placeholder': 'Username',
			}),
		'email': forms.EmailInput(attrs ={
			'class': 'input--style-4',
			'placeholder': 'Email',
			}),
		}


	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(
			attrs = {
			'class': 'input--style-4', 'placeholder':'Password'
			})
		self.fields['password2'].widget = forms.PasswordInput(
			attrs = {
			'class':'input--style-4', 'placeholder': 'Confirm Password'
			})