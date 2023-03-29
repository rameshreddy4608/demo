from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app(request):
    return HttpResponse('<h1>this my is my first project<h1>')