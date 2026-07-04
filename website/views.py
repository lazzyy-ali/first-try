from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return render(request,'index.html')

def about_view(request):
     return render(request,'home.html')

def contact_view(request):
     return render(request,'contact.html')