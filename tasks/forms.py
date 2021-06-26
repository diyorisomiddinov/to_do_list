from django import forms

from tasks.models import TaskModel


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['title']
