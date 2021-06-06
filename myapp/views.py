from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from myapp.forms import TodoForm
from myapp.models import TodoTask

# Create your views here.
def index(request):

    context = {'success': False}
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            task = form.cleaned_data['task']
            f_save = TodoTask(title = title, task = task)
            f_save.save()
            return redirect('/task')

    form = TodoForm()
    context = {
            "form":form,
            "success": True
        }
        
    return render(request, 'index.html', context)


def task(request):
    data = TodoTask.objects.all()
    context = {
        'data':data
    }
    return render(request, 'task.html', context)

def deletetask(request, id):
    _delete = TodoTask.objects.get(id=id)
    _delete.delete()
    return HttpResponseRedirect('/task')

def update(request,id):
    context = {'success': False}
    form = TodoTask.objects.get(id=id)
    if request.method == "POST":
        form.title = request.POST['title']
        form.task = request.POST['task']
        form.save()
        return redirect('/task')
    form = TodoForm(instance=form)

    context = {
        "form": form,
        "success": True
    }
    return render(request, 'update.html', context)