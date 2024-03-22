from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'finances/home.html',context ={
        'name': 'rogax',
    })
def Grafics(request):
    return HttpResponse('grafics')

def contact(request):
    return HttpResponse('Contact')
