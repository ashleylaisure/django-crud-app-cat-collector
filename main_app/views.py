from django.shortcuts import render, redirect
# Import HttpResponse to send text-based responses
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cat, Toy
from .forms import FeedingForm


# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]

# Create your views here.
# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('<h1>About the Cat Collector</h1>')
    return render(request, 'about.html')

def cat_index(request):
    # Render the cats/index.html template with the cats data
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats' : cats})

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    toys = Toy.objects.all()  # Fetch all toys
    # Only get the toys the cat does not have
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))

    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'cat' : cat,
        'feeding_form' : feeding_form,
        'toys' : toys_cat_doesnt_have,
        })

def add_feeding(request, cat_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('cat-detail', cat_id=cat_id)


class CatCreate(CreateView):
    model = Cat
    # fields = '__all__'
    # can list the fields availiable to the user
    fields = ['name', 'breed', 'description', 'age']
    # success_url = '/cats/' redirect to index
    # Remove success_url so Django uses get_absolute_url from Cat
    
class CatUpdate(UpdateView):
    model = Cat
    fields = ['breed', 'description', 'age']
    
class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'
    
class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy
    
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cat-detail', cat_id=cat_id)

def remove_toy(request, cat_id, toy_id):
    # Look up the cat
    # Look up the toy
    # Remove the toy from the cat
    Cat.objects.get(id=cat_id).toys.remove(toy_id)
    return redirect('cat-detail', cat_id=cat_id)
