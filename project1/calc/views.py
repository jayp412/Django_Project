from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'JJJJJJJJJJ'})

def addtion(request):
    return render(request,'result.html',{'result':int(request.POST['n1'])+int(request.POST['n2'])})