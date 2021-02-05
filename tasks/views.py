from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    login_url = 'login'

    def get_queryset(self):
        obj = Task.objects.all()
        return obj.filter(created_by=self.request.user)
        

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_create.html'
    fields = ('title', 'content',)
    login_url = 'login'

    def form_valid(self, form): # new
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_update.html'
    fields = ('title','content',)
    login_url = 'login'

    def get_success_url(self):
        return reverse('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')