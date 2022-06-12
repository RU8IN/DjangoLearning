# Project setup #

<br>

Firstly, we need to start a new project. We can choose the folder we like and start there. 


```Python
python -m venv venv (or any other folder name)
```

It is virtual environment. You need it to diverse your projects with different libraries.

```
cd venv/Scripts
./activate
```

After this step, we can download various libraries into the python virtual environment without any difficulties.

```
pip install django
```



We need to install django library.

```
django-admin startproject projectname
```
<br>

Looking ahead, when you already started your project, write
```
pip freeze > requrements.txt
```
to save your dependencies to ```requirements.txt``` file

```
pip install -r requrements.txt
```
to install all dependencies.

<br>
<br>

## Manage.py ##

Manage.py is the command-line program that we will use very often.

Here's most used commands:
```
python.exe manage.py runserver
```
Obviously
```
python.exe manage.py makemigrations
```
Makes preparations that will be applied to database
```
python.exe manage.py migrate
```
Applies changes to database
```
python.exe manage.py startapp appname
```
Creates new folder with app name. Files like urls.py should be added manually.
<br>
<br>

## Rendering
<br>
Django can render different pages with functions or classes. It is usually easier to make classes based on models, but if you need one small page you can make render function.

<br>

In ```views.py``` we add new function that will render our new page with ```request``` argument.

```Python
def first_page(request):
    return render(request, 'template_name', {})
```
Built-in function render has standard arguments: 

```request``` - request object

```template_name``` - name of the HTML file that should be used for rendering.

```{}``` - dictionary that will be used by django in purposes of rendering page

<br>

### HTML Templates

Firstly, you have to add default templates folder to project settings file. In ```project_name/settings.py``` we add template_folder_name to 



```Python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates_folder'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
Also ```APP_DIRS``` must be set to ```True```

Then we add HTML file to our templates folder and write change template_name in ```first_page()``` function.


<br>
<br>

## Static Files

In ```settings.py``` make sure that line
```Python
django.contrib.staticfiles
``` 
presents in ```INSTALLED_APPS```

and 
```Python
STATIC_URL = '/static/'
```
in the end of file (in fact, it doesn't matter where, it's just more convenient).


# Models

Django uses models to interact with database.
We will use sqlite3. It is simple itself and suits perfectly for simple projects.

Models should be written in ```models.py``` file in app directory. 

Example:
 
```Python
class BaseEvent(models.Model):

    title = models.CharField(verbose_name = "title",max_length=155)
    description = HTMLField(verbose_name = "description", max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/',
                              height_field=None, width_field=None, max_length=100)
    slug = models.SlugField(verbose_name="slug", max_length=100)
    created = models.DateTimeField(verbose_name = "creation date", auto_now_add=True)
    published = models.BooleanField(verbose_name = "publication date", )
    author = models.ForeignKey(AUTH_USER_MODEL, related_name="%(class)s_related", on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
```

In this example we can see that this class is inherited from Model class. It is necessary for django.

All model field types can be found in django documentation.


<br>
<br>

```Python
class Meta:
    abstract = true
```
It is necessary to make it clear to django that this class is the base for the rest. In simple sites, it is not used very often, but it depends on the task.
Given here as an example to give an understanding about overriding built-in class parameters in django.



<br>
<br>

### Changes

By executing makemigrations command you can make special files (will be automatically  stored in migrations folder in every app folder) that will give django understanding of what you want database to be. After every change of models.py you should write
```
python manage.py makemigrations
python manage.py migrate
```
to apply changes to database.

<br>
<br>

# Class based views

```Python
class SampleModelView(ListView):
    model = SampleModel
    context_object_name = 'samples'
    template_name='class_view_test.html'
```

As you can see in this example, class based views are more concise and easy to understand. You just have write model that this class will render, template and context name. You will use this context name in django template. In this special case of ListView it will be like
```Django
{% for sample in samples %}

{{ sample.username }}

{% endfor %}
```

By using django templates we can paste our data in this html file every moment user renders the page. 
There can be different types of view. TemplateView, ListView, DetailView, CreateView, DeleteView and others. This kinds of View can do different actions to object in database.

```DetailView``` - renders one specific object

```DeleteView/CreateView``` - renders page that will give user possibility to delete/create specific object

```ListView``` - renders page that will show a lot of objects to user

There is a lot of ways to configure views files. 