from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm
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
    id_list = finch.toys.all().values_list('id')
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, "main_app/finches/detail.html", {'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have})


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    # validate form
    if form.is_valid():
        # dont save form to db until it has finch_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)


def unassoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'color', 'description', 'age']

    # success_url = 'finches/{finch_id}'


class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a finch by excluding the name field!
    fields = ['color', 'description', 'age']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'


class ToyIndex(ListView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyDetail(DetailView):
    model = Toy


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'


class ToyUpdate(UpdateView):
    model = Toy
    fields = '__all__'
