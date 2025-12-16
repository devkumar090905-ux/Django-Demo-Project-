from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import ExampleModel
from .forms import ExampleForm

# Create your views here.
def index(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        example = ExampleModel(name=name, email=email, number=number)
        example.save()


    context = {
        "variable":"this is home page"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is home page")

def show_data(request):
    data = ExampleModel.objects.all()
    return render(request,'show.html',{'data':data})

def update_data(request,id):
    obj = ExampleModel.objects.get(id=id)
    if request.method == "POST":
        form = ExampleForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_data')
    else:
        form = ExampleForm(instance=obj)
        
    return render(request,'update.html',{'form':form})

def delete_data(request,id):
    obj = ExampleModel.objects.get(id=id)
    obj.delete()
    return redirect('show_data')