from django.shortcuts import render
from .models import Destination
# Create your views here.


def index(request):
    dest1=Destination.objects.all()
    return render(request,'index.html',{'dests':dest1})