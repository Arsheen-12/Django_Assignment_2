from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def task_list(request):
        tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'create_task.html', {'form': form})

def delete_task(request, id):
    post = Task.objects.get(id=id)
    post.delete()
    return redirect('task_list')
