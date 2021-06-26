from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from tasks.forms import TaskModelForm
from tasks.models import TaskModel


class TaskCreateView(CreateView):
    template_name = 'index.html'
    form_class = TaskModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = TaskModel.objects.all()
        return context

    def get_success_url(self):
        return reverse('create')


def check(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)

    if task.is_active:
        task.is_active = False
    else:
        task.is_active = True

    task.save()

    return redirect('/')
