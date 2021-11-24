from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'sili.html')

def sili(request):
    #return HttpResponse("SILI")
    return render(request, 'sili.html')
# Create your views here.
