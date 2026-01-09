
# Django Documentation

``` Django is a high-level, open-source Python web framwork used for developing secure, scalable, and maintainable web application rapidly.It fallows the MVT (Model-View-Template) architecture and is based on the "Don't REpeat Yourself"```

## 1. These are simple steps to build django project

### Stap 1: You have to open directry on cmdand install Django.
```
pip install Django
```

### Stap 2: Install project of Django

```
django-admin startproject <project_name>
```

### Stap 3: Run your project 

```
cd <project_name>
python namage.py runserver <port>
(By default 8000)      
```
### Stap 4: Run your project on Browser
```
localhost:<port>
```
- Now you can see a rocket in front of you. Is Rocket lounched mean your project installed.

### Stap 5: goto terminal -> ctrl+c -> to quit the server then, create a new app
```
django-admin startapp <app_name>
```
### Stap 6: Go to  cmd -> Enter  **code .** -> open your project on vs code restart project
```
python manage.py runserver <port>
```
### Stap 7: Goto urls.py (inside <project_name>) ->by defult you see one route->"admin" -> check admin route you have / admin after localhost: <port> as localhost: <port>/admin

### Stap 8: Now , we need create our own page on blank url so we need to addone more item urlpatterns list.

```
Syntex 
		path('<url>',view.<funtion_name>),
		eg:
		path('',views.index),
```

```
Errors:
        err1:views not defined
		sol :from<app_>import views
		err2:<app_name>.views don't have '<fun_name>' attribute
```
- Error 2nd solution in stap 9.

### Stap 9: Goto views.py of <app_name> now creat a new funtion.
-  Youshoud take minimum one parameter commonly  that paremeter name is request 
- firstly we only use return render(request,'<filename>.html')

```
Example: def <funtion_name>(request):
                return render(request,'index.html')
```

- Now go to your brawser and refresh , now you can see the error templates does'nt exist.


### Stap 10: Now you have to creat a new folder inside <app_name> templates now create <filename.html> inside templates folder

### Stap 11: Now you need to establish connection b/w project and app -> goto setting.py(inside project) -> check line 33 you will list ofinstalled app add your app in this list '<app_name>'

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',  # Custom app (Home is app name)
]
```
### Stap 12: Now, refresh your web page you will see nothinf a blank page congratulation you have create your own page n Diago project.

### Stap 13:creat a new folder beside templates inside <app_name> by static name which is used for assets of our project now,creat css folder inside static and after this create style.css file inside css folder now, write css code.

### Stap 14:To pick your css with html you can use tag and for path of css file you should use ginger template ({% %}) of static something like this:

```
	(%static 'css/style.css'%)
```

### Stap 15: Refresh your webpage is you see red color on you webpage means you have success linked your css on html page.
		
### Stap 16: Now you can create SuperUser for access your admin panel.
```
	python manage.py createsuperuser
```
#### Enter these deteils
- Username : 
- Email address:
- Password:
- Password (again):
- This password is too short. It must contain at least 8 characters.
- Bypass password validation and create user anyway? [y/N]: y

- Superuser created successfully.

### Stap 17: Now you can run these command 
```
python manage.py makemigrations
python manage.py migrate
```

- output of first command.

```
No changes detected
```
- output of second command.

```
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
## 2. Save data in database.

### Stap 1: go to models.py and create data base.
```
from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    number = models.IntegerField()
```
- ExampleModel means database ka nam isme hamne 3 row banai hai data ko save karne ke liye.
- is file me ham data type ko bhi defain karte hai.


### Stap 2: go to admin and ragister your database.

```
from django.contrib import admin
from home.models import ExampleModel

# Register your models here.
admin.site.register(ExampleModel)

```
### Stap 3: Run tow command .
```
python manage.py makemigrations
python manage.py migrate
```


### Stap 4: go to app/views.py file and enter details like.
```
def index(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        example = ExampleModel(name=name, email=email, number=number)
        example.save()

    return render(request, 'index.html')
```

- isme index ak funtion hai jise url call karta hai 
- is file li help se data ko database me sahi series me save kiya jata hai.
- example databse ka nam hai.
- example.save() ka matlb data ko save kar dena database me.


### Stap 5: go to your html file and make a form and make sour you have a name attribute 

```
Example: 
   <form method="POST" action="/">
        {% csrf_token %}    
        <div class="mb-3">
            <label for="name" class="form-label" name="name"> Enter your name</label>
            <input  class="form-control" id="name" name="name" >
        </div>
        <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" id="email" name="email">
            <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        
        <div class="mb-3">
            <label for="nnumber" class="form-label">PassEnter your number</label>
            <input type="number" class="form-control" name="number" id="number">
        </div>

        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
```

**name attribute se hi data ko database me save karaya jata hai.**


-  {% csrf_token %} likhna medetry hai.


### Stap 6: Run the server and save the data the go to admin panel and check data hai ya nahi.


## 3. How to fatch your data in web page.

### Stap 1: create new template show.html
### Stap 2: go to urls add the path 

```
    path('show/',views.show_data,name='show_data'),
```
### Stap 3: go to views.py and write code.
```
  def show_data(request):
    data = ExampleModel.objects.all()
    return render(request,'show.html',{'data':data})
```
### Stap 4: write code in show.html

```
 <table border="1">
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Number</th>
        </tr>
        {% for i in data %}
        <tr>
            <td>{{i.name}}</td>
            <td>{{i.email}}</td>
            <td>{{i.number}}</td>
        </tr>
        {% endfor %}
    </table>
```
### Stap 4: run the server and check data hai ya nahi.

## 4. How to add Edit and delete button.


### Stap 1: Add path in urls.py 

```
 path('update/<int:id>',views.update_data,name='update_data'),
 path('delete/<int:id>',views.delete_data,name='delete_data'),
```

### Stap 2: Add function in views.py and write code.

```
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
```
- this is for Edit data.

```
def delete_data(request,id):
    obj = ExampleModel.objects.get(id=id)
    obj.delete()
    return redirect('show_data')
```
- and this is for delete data.

### Stap 3: add code in html file.

```
                <a href="{% url 'update_data' i.id %}">
                    <button>Edit</button>
                </a>
                <a href="{% url 'delete_data' i.id %}" onclick="return confirm('Are you sure?')">
                    <button>Delete</button>
                </a>
```

### Stap 4: Now you can run your project and check it.









