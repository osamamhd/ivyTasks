from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
