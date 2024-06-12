from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# item view.
def item(request):
    return HttpResponse("This is the item view")