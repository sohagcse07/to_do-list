from django.shortcuts import render, redirect, get_object_or_404
from .forms import Taskfrom
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = Taskfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = Taskfrom()
    return render(request, 'todo/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = Taskfrom(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = Taskfrom(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')
