from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Task, TaskModelForm

def task_list(request):
    tasks = Task.objects.order_by('-priority', 'date')
    return render(request, 'task_list.html', {"tasks": tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskModelForm()
    return render(request, 'task_form.html', {"form": form, "title": "Create Task"})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskModelForm(instance=task)
    return render(request, 'task_form.html', {"form": form, "title": "Update Task"})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {"task": task})