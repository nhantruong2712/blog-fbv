from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from user import views

app_name = 'user'

urlpatterns = [
	path('activationSent/', views.activation_sent, name='activationSent'),
	path('register/', views.register, name='register'),
	path('login/', views.logincase, name="login"),
	path('activate/<uidb64>/<token>/', views.activate, name='activate'),
	path('logout/', views.logoutuser, name='logout'),
]



