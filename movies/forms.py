from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from crispy_forms.layout import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

class CustomCheckbox(Field):
    template = 'custom_checkbox.html'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email', 'password1', 'password2']
		widgets = {
		'username':forms.TextInput(attrs ={
			'placeholder': 'Username',
			}),
		'email': forms.EmailInput(attrs ={
			'placeholder': 'Email',
			}),
		}

	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
		CustomCheckbox('check_me_out')
		)
		self.fields['password1'].widget = forms.PasswordInput(
			attrs = {
			'class': 'input--style-4', 'placeholder':'Password'
			})
		self.fields['password2'].widget = forms.PasswordInput(
			attrs = {
			'class':'input--style-4', 'placeholder': 'Confirm Password'
			})
		self.helper.form_show_labels = False



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False
# input--style-4

