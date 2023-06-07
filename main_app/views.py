from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Finch
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
    feeding_form = FeedingForm()
    return render(request, "main_app/finches/detail.html", {'finch': finch, 'feeding_form': feeding_form})


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    # validate form
    if form.is_valid():
        # dont save form to db until it has finch_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
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
