from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django import template
def home(request):
        return HttpResponse(u'Привет, Мир!', content_type="text/plain")
def home(request):
 return render(request, 'templates/index.html')