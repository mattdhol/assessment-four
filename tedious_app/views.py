from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.db.models import Sum
import operator

def home(request):
  return render(request, "home.html")

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"

class TaskDelete(DeleteView):
  model = Task
  success_url = "/home/"

def task_index(request):
    task = Task.objects.all()
    sum_time = task.aggregate(Sum('time'))
    print(sum_time)
    sum_timee = sum_time['time__sum']
    print(sum_timee)
    return render(request, 'home.html', 
    {'task': task, 'sum_timee': sum_timee})


def task_detail(request):
    task = Task.objects.get(id=task_id)
    return render(request, 'task/detail.html', 
    {'task': task})