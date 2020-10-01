from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Todo


# Create your views here.
def index(request):
    todo_items = Todo.objects.all().order_by("added_date").reverse()
    return render(request, 'todo/index.html', {"todo_items": todo_items})

def add_todo(request):
  current_date = timezone.now()
  content = request.POST["content"]
  Todo.objects.create(added_date=current_date, text=content) #add database
  todo_items = Todo.objects.all().order_by("added_date")
  return HttpResponseRedirect("/")
