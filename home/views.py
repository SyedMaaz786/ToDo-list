from django.shortcuts import render, redirect, get_object_or_404
from home.models import Task

def home(request):
    context = {'success': False}
    if request.method == 'POST':
        # Handle the form
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)
def tasks(request):
    query = request.GET.get('search', '')  # Get search input from URL
    if query:
        allTasks = Task.objects.filter(taskTitle__icontains=query)
    else:
        allTasks = Task.objects.all()
    context = {'tasks': allTasks, 'search_query': query}
    return render(request, 'tasks.html', context)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')

def toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = not task.status   # Flip True/False
    task.save()
    return redirect('tasks')

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.taskTitle = request.POST.get('title')
        task.taskDesc = request.POST.get('desc')
        task.save()
        return redirect('tasks')

    context = {'task': task}
    return render(request, 'edit_task.html', context)
