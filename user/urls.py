from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from user import views

app_name = 'user'

urlpatterns = [
	path('activationSent/', views.activation_sent, name='activation_sent'),
	path('register/', views.register, name='register'),
	path('login/', views.logincase, name="login"),
	path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
	path('logout/', views.logoutuser, name='logout'),

]



