from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisement.objects.all()
    contex = {'advertisements':advertisements}
    return render(request, 'index.html', contex)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def register(request):
    return render(request, 'register.html')

def advertisement_post(request):
    form = AdvertisementForm()
    context = {'form':form}
    return render(request, 'advertisement-post.html', context)