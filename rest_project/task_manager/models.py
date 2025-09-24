from django.db import models
from django import forms

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=255)
    assignee = models.CharField(max_length=255)
    date = models.DateField()
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.task} ({self.assignee})"


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task", "assignee", "date", "priority"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }