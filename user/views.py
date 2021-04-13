from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.core import mail

from user.forms import Register
from user.tokens import account_activation_token
# Create your views here

def register(request):
	regisForm = Register(request.POST)
	if regisForm.is_valid():
		user = regisForm.save()
		user.refresh_from_db()
		# user.profile.first_name = regisForm.cleaned_data.get('first_name')  # cleaned_data is holding
		# user.profile.last_name = regisForm.cleaned_data.get('last_name')  # the validated form data
		user.profile.email = regisForm.cleaned_data.get('email')
		user.is_active = False  # user can't login until confirm link
		user.save()
		current_site = get_current_site(request)
		subject = "Please Active Your Account"

		message = render_to_string('user/activate_request.html', {
			'user': user,
			'domain': current_site.domain,
			'uid': urlsafe_base64_encode(force_bytes(user.pk)),
			# method will generate a hash value with user related data
			'token': account_activation_token.make_token(user),
		})
		plain_message = strip_tags(message)
		# user.email_user(subject, plain_message)
		mail.send_mail(subject, plain_message, 'From Nhandzblog <nhandzblog@gmail.com>', [user.profile.email], html_message=message)
		# login(request, user)  # use when don't need to email confirm
		# login() method takes an HttpRequest object and a User object and saves the user’s ID in the session
		return redirect('/accounts/activationSent')
	# else:
	# 	regisForm = Register()    # cannot show the error message if use else
	context = {'regisForm': regisForm}
	return render(request, 'user/register.html', context)


def logincase(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				# redirect to previous page after login
				if 'next' in request.POST:
					return redirect(request.POST.get('next'))
				else:
					return redirect('/')
			else:
				messages.info(request, "Username or password is incorrect. Did you active or create account?")
	context = {}
	return render(request, 'user/login.html', context)


def activation_sent(request):
	return render(request, 'user/activation_sent.html')


def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	# checking if the user exists, if the token is valid.
	if user is not None and account_activation_token.check_token(user, token):
		# if valid set active true
		user.is_active = True
		# set signup_confirmation true
		user.profile.signup_confirmation = True
		user.save()
		login(request, user, backend='django.contrib.auth.backends.ModelBackend')
		return redirect('/accounts/login')
	else:
		return render(request, 'user/activation_invalid.html')


@login_required(login_url='/accounts/login')
def logoutuser(request):
	logout(request)
	return redirect('/accounts/login')
