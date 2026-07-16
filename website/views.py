from django.shortcuts import render
from django.http import HttpResponse
from website.models import contact
from website.forms import NameForm, ContactForm
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
     return render(request,'website/about.html')

def contact_view(request):
     if request.method=='POST':
          form = ContactForm(request.POST)
          if form.is_valid():
               form.save()
               messages.add_message(request,messages.SUCCESS,'your token submit is sucsesfull')
          else:
               messages.add_message(request,messages.ERROR,'your token submit is not sucsesfull')   
     
     form = ContactForm()
     return render(request, 'website/contact.html', {'form':form})


def test_view(request):
     if request.method== 'POST':
          form = ContactForm(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponse('done')
          else:
               return HttpResponse('not valid')
     
     form = ContactForm()
     return render(request, 'test.html', {'form':form})
