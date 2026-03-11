from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def home(request):

    all_tasks = Task.objects.all()

    return render(request, 'home.html', {'tasks': all_tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]

        task = Task.objects.create(
            title = title,
            description = description
        )

        return redirect('home')

    return render(request, 'add.html')

def update(request, task_id):
    task = Task.objects.get(id = task_id)
    
    if request.method == "POST":
        title = request.POST.get('title', default="Title")
        description = request.POST.get('description', default="Description")

        task.title = title
        task.description = description
        task.save()

        return redirect('home')

    return render(request, 'update.html', {'task':task})

def mark_complete(request):

    return render(request, 'complete.html')