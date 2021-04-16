from django.urls import path, include, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from user import views

app_name = 'user'

urlpatterns = [
	# path('', include('django.contrib.auth.urls')),
	path('activationSent/', views.activation_sent, name='activationSent'),
	path('register/', views.register, name='register'),
	path('login/', views.logincase, name="login"),
	path('activate/<uidb64>/<token>/', views.activate, name='activate'),
	path('logout/', views.logoutuser, name='logout'),

	# custom interface auth_views
	path('password_change/', auth_views.PasswordChangeView.as_view(
		template_name='registration/html_password_change_form.html'), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
		template_name='registration/html_password_change_done.html'), name='password_change_done'),
	path('password_reset/', auth_views.PasswordResetView.as_view(
		template_name='registration/password_reset.html',
		html_email_template_name="registration/html_password_reset_email.html"), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
		template_name='registration/password_reset_sent.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
		template_name='registration/html_password_reset_confirm.html'), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
		template_name='registration/html_password_reset_complete.html'), name='password_reset_complete'),

]



