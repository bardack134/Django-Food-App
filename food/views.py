from django.http import HttpResponse
from django.shortcuts import render
from .models import DessertsItems, DrinksItems, Item, SidesItems
from django.shortcuts import get_object_or_404, render

# Create your views here.
def home(request):
    
    # Retrieve all objects from the 'Item' model and assign them to 'item_list'
    item_list = Item.objects.all()
    
    # Retrieve all objects from the 'DrinksItems' model and assign them to 'DrinksItems_list'
    drinksItems_list = DrinksItems.objects.all()
    
    # Retrieve all objects from the 'dessertsItems' model and assign them to 'dessertsItems_list'
    dessertsItems_list = DessertsItems.objects.all()
    
    # Retrieve all objects from the 'SidesItems' model and assign them to 'SidesItems_list'
    sidesItems_list = SidesItems.objects.all()

    context = {
        "item_list": item_list,
        "drinksItems_list": drinksItems_list,
        "dessertsItems_list": dessertsItems_list,
        "sidesItems_list": sidesItems_list,
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



#TODO:1. create the models where we will store the information about the products offered by the restaurant (main, drinks..etc)

#TODO: 2. create the home page and render all the products in the page

#TODO: 3. Create a view called details.html to see the details of the products, in my case the details of the products are seen
# in the modal window

#TODO: 4. Create the cart in the nav bar

#TODO: when you press the add to cart button the products should be added to the cart





#TODO: DEBE HABER UNA PAGINA CON LOS DETALLES DE LA COMPRA QUE SE VA HACER
#TODO: CREAR USER SYSTEM

