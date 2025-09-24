from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import Task, TaskModelForm
from django.db.models import Count, Avg
import requests
import json


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



def report(request):
    by_assignee = (
        Task.objects.values('assignee')
        .annotate(total=Count('id'))
        .order_by('-total', 'assignee')
    )
    assignee_labels = [row['assignee'] for row in by_assignee]
    assignee_totals = [row['total'] for row in by_assignee]

    by_priority = (
        Task.objects.values('priority')
        .annotate(total=Count('id'))
        .order_by('priority')
    )
    priority_labels = [str(row['priority']) for row in by_priority]
    priority_totals = [row['total'] for row in by_priority]

    context = {
        'assignee_labels_json': json.dumps(assignee_labels),
        'assignee_totals_json': json.dumps(assignee_totals),
        'priority_labels_json': json.dumps(priority_labels),
        'priority_totals_json': json.dumps(priority_totals),
        'title': 'Task Report',
    }
    return render(request, 'report.html', context)


def external_posts(request):
    """
    Example integration: fetch posts from a third-party API (JSONPlaceholder)
    and display a few fields. Handles basic errors gracefully.
    """
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    posts = []
    error_message = None
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        # Limit to first 10 items for brevity
        posts = response.json()[:10]
    except requests.RequestException as exc:
        error_message = f"Failed to load external data: {exc}"

    return render(request, 'external_posts.html', {
        'title': 'External Posts (JSONPlaceholder)',
        'posts': posts,
        'error_message': error_message,
    })