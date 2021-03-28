from django.urls import path

from todoapp import views

app_name = 'todoapp'

urlpatterns = [
	path('todo', views.index, name='index'),
	path('add', views.add, name='add'),
	path('delete-all', views.delete_all, name='delete_all'),
	path('delete-complete', views.delete_complete, name='delete_complete'),
	path('complete/<todo_id>', views.complete, name='complete'),
]