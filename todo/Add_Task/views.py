from django.shortcuts import redirect, render
from .models import task
from . import views
# Create your views here.
def index(request):
    t = task.objects.all()
    return render(request, 'index.html', {'t' : t})

def add_task(request):
    if request.method == 'POST':
        t1 = task()
        t1.task_name = request.POST.get('Task_name')
        t1.task_date = request.POST.get('date')
        t1.task_time = request.POST.get('Time')
        t1.task_des = request.POST.get('des')
        t1.work_done = "False"
        t1.save()

    return redirect('/')

def work_done(request):
        if request.method == 'POST':
            value = request.POST.get('id')
            task.objects.filter(id=value).delete()
            return redirect('/')