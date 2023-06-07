from django.shortcuts import render
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
