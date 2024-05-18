from django import forms
from django.shortcuts import get_object_or_404, render,redirect,HttpResponseRedirect
from django.urls import reverse
from .models import aboutinfo,whychoose,ouerservice,customer,contact
from .forms import ContactForm

def index(request):
  about = aboutinfo.objects.all()
  why = whychoose.objects.all()
  service =ouerservice.objects.all()
  cust = customer.objects.all()

 
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()



  context ={
    'abouts':about,
    'whys':why,
    'service':service,
    'customer':cust,
    'form':form
    
    
    
  }
  return render(request, 'index.html',context)

# def my_form_view(request):
 
# return render(request, 'index.html')

    