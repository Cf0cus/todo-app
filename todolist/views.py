from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Task
from django.urls import reverse
from django.utils import timezone

def todo(request):
    task_list = Task.objects.filter(status = False)
    
    return render(request,"todolist/todoview.html",{"task_list":task_list})


def add_task_page(request):
    return render(request,"todolist/addtodo.html")


def save_task(request):
    task_desc = request.POST["task_desc"]
    pub_date = timezone.now()
    status = False

    added_task = Task(task_desc=task_desc,status=status,pub_date=pub_date)
    added_task.save()

    return HttpResponseRedirect(reverse("todolist:todoview"))

def update_task(request):
    task_list_updated = request.POST.getlist("task")
    for task_id in task_list_updated:
        task = get_object_or_404(Task,pk=task_id)
        task.status = True
        task.save()
    
    return HttpResponseRedirect(reverse("todolist:todoview"))
