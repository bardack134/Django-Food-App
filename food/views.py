from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from django.shortcuts import get_object_or_404, render

# Create your views here.
def home(request):
    item_list=Item.objects.all()
    context = {
        "item_list": item_list
        }
    return render(request, "food/index.html", context)
    

# item view.
def item(request):
    return HttpResponse("This is the item view")


# detail view.
def detail(request, item_id):
    item=get_object_or_404(Item, pk=item_id)
    context = {
        "item": item
        }
    return render(request, "food/details.html", context)