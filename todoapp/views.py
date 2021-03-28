from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from todoapp.forms import TodoForm
from todoapp.models import Todo

# Create your views here.


def index(request):
	todo_list = Todo.objects.order_by('id')
	forms = TodoForm

	context = {'forms': forms, 'todo_list': todo_list}
	return render(request, 'todoapp/todo.html', context)

@require_POST
def add(request):
	form = TodoForm(request.POST)

	if form.is_valid():
		new_todo = Todo(title=request.POST['title'])
		new_todo.save()

	return redirect('/todoapp/todo')


def complete(request, todo_id):
	complete = Todo.objects.get(pk=todo_id)
	complete.is_complete = True
	complete.save()

	return redirect('/todoapp/todo')


def delete(request, todo_id):
	Todo.objects.filter(pk=todo_id).delete()

	return redirect('/todoapp/todo')


def delete_complete(request):
	Todo.objects.filter(is_complete__exact=True).delete()

	return redirect('/todoapp/todo')


def delete_all(request):
	Todo.objects.all().delete()

	return redirect('/todoapp/todo')