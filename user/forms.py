from django import forms
from django.contrib.auth.backends import AllowAllUsersModelBackend
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


class Register(UserCreationForm):
	first_name = forms.CharField(max_length=32)
	last_name = forms.CharField(max_length=32)
	email = forms.EmailField(max_length=100)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

		# commit = True : save instance to db
		def save(self, commit=True):
			user = super(Register, self).save(commit=False) # not save instance, you can custom before save
			user.first_name = self.cleaned_data['first_name']
			user.last_name = self.cleaned_data['last_name']
			user.email = self.cleaned_data['email']
			user.password1 = self.cleaned_data['password1']
			user.password2 = self.cleaned_data['password2']
			if commit:
				user.save()
			return user

		# Check if exist email
		def clean_email(self):
			username = self.cleaned_data.get('username')
			email = self.cleaned_data.get('email')
			# exclude: Returns a new QuerySet containing objects that do not match the given lookup parameters.
			if email and User.objects.filter(email=email).exclude(username=username).exists():
				raise forms.ValidationError("This email is already in use! Try another email.")
			return email

		# Check if exist username
		def clean_username(self):
			username = self.cleaned_data.get('username')
			email = self.cleaned_data.get('email')
			# exclude: Returns a new QuerySet containing objects that do not match the given lookup parameters.
			if username and User.objects.filter(username=username).exclude(email=email).exists():
				raise forms.ValidationError("This username is already in use! Try another username.")
			return username

# Allow only for active users
class PickyAuthenticationForm(AuthenticationForm):
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username is not None and password:
			backend = AllowAllUsersModelBackend()
			self.user_cache = backend.authenticate(self.request, username=username, password=password)
			if self.user_cache is None:
				raise self.get_invalid_login_error()
			else:
				self.confirm_login_allowed(self.user_cache)

		return self.cleaned_data

	def confirm_login_allowed(self, user):
		if not user.is_active:
			raise forms.ValidationError(("This account is inactive."), code='inactive',)
		return HttpResponse("Please active your account")