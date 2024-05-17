from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoItemForm

def index(request):
    return redirect('todo_list')

def todo_list(request):
    todos = ToDoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoItemForm()
    return render(request, 'todo/create_todo.html', {'form': form})

def delete_todo(request, todo_id):
    todo = ToDoItem.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')
