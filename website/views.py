from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>home page</h1>')

def about_view(request):
    return HttpResponse ('<h1> about view </h1>')

def contact_view(request):
    return HttpResponse ('<h1> contact view </h1>')