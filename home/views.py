from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import ExampleModel
from .forms import ExampleForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        user = ExampleModel.objects.filter(name=name,email=email).first()
        if user:
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('login')
        else:
            return render(request,'index.html',{'error': 'Invalid name or email'})
 
    return render(request,'index.html')


def form(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        example = ExampleModel(name=name, email=email, number=number)
        example.save()


    context = {
        "variable":"this is home page"
    }
    return render(request, 'form.html',context)
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

@login_required(login_url='login')
def login(request):
    if 'user_id' not in request.session:
        return redirect('index')
    return render(request,'login.html')