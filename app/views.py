from django.shortcuts import render,redirect
from .models import Todo
from django.shortcuts import get_object_or_404
from .forms import TodoModelForm



# Create your views here.
def index(request):
    items = Todo.objects.all()
    form = TodoModelForm()
    context = {'todos':items,'form':form}
    return render(request,'app/index.html',context)


def add(request):
    form = TodoModelForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')
        
    


def completed(request,id):
    obj = get_object_or_404(Todo,pk = id)
    obj.completed = True
    obj.save()
    return redirect('/')
    
def delete(request,id):
    obj = get_object_or_404(Todo,pk = id)
    obj.delete()
    return redirect('/')
    
