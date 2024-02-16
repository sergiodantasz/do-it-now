from django.contrib.messages import error, success
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from tasks.forms import TaskForm
from tasks.models import Task


@login_required(login_url='users:login')
def tasks(request):
    user_tasks = Task.objects.filter(user=request.user)
    context = {
        'title': 'Do It Now',
        'tasks': user_tasks,
        'show_labels': False,
    }
    data = request.session.get('data')
    form = TaskForm(data)
    context['form'] = form
    context['action'] = reverse('tasks:create')
    return render(request, 'tasks/pages/base.html', context)


@login_required(login_url='users:login')
def mark_task_as_done(request):
    redirect_url = redirect(reverse('tasks:tasks'))
    if not request.POST:
        error(request, 'An error occurred while marking the task as done.')
        return redirect_url
    task_id = request.POST.get('id')
    task = Task.objects.get(id=task_id)
    task.delete()
    success(request, 'Task marked as done.')
    return redirect_url


@login_required(login_url='users:login')
def create_task(request):
    redirect_url = redirect(reverse('tasks:tasks'))
    if not request.POST:
        error(request, 'An error occurred while creating the task.')
        return redirect_url
    request.session['data'] = request.POST
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        del request.session['data']
        success(request, 'Task created.')
    return redirect_url
