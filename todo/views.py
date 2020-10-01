from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST

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

@require_POST
def delete_todo(request,todo_id):
  #todo = get_object_or_404(Todo, id=todo_id)
  #todo.delete()    
  Todo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect("/")
