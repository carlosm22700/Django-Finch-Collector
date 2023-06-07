from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Finch
# Create your views here.


def home(request):
    return render(request, 'main_app/home.html')


def about(request):
    return render(request, 'main_app/about.html')


def finch_index(request):
    finches = Finch.objects.all()
    return render(request, 'main_app/finches/index.html', {'finches': finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, "main_app/finches/detail.html", {'finch': finch})


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'color', 'description', 'age']

    # success_url = 'finches/{finch_id}'


class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['color', 'description', 'age']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'
