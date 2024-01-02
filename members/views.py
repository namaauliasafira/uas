from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

# def work(request):
#   template = loader.get_template('work.html')
#   return HttpResponse(template.render())
# def contact(request):
#   template = loader.get_template('contact.html')
#   return HttpResponse(template.render())

