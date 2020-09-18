from django_unicorn.components import UnicornView
from django import forms


class TodoForm(forms.Form):
    task = forms.CharField(min_length=1, max_length=255, required=True)


class TodoBulmaView(UnicornView):
    form_class = TodoForm

    task = ""
    tasks = []

    def add(self):
        if self.is_valid():
            self.tasks.append(self.task)
            self.task = ""
