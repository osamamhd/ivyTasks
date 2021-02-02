from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_create.html'
    fields = ('title', 'content')

    def get_success_url(self):
        return reverse('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    fields = ('title','content',)

    def get_success_url(self):
        return reverse('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')