from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def just(request):
    return HttpResponse("this is VS mart site")

def home(request):
    return render(request,'home.html')



