from django.shortcuts import render

from todos_app.forms import TodoForm
from todos_app.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
        'todo_form': TodoForm(),
    }

    return render(request, 'todos_app/index.html', context)
