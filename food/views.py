from django.http import HttpResponse
from django.shortcuts import redirect, render
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


"""VIEWS FOR THE SHOPPING CART"""
from .cart import Cart


def cart(request):
    """
    View to display the shopping cart
    """
    return render(request, 'cart.html')


def add_item(request, product_id):
    """
    Add a Product to Cart
    """
    
    if request.method == 'POST':
        
        # Get the quantity of the product from the form and convert it to an integer.
        quantity = int(request.POST['quantity'])
    
    # If is a GET request, set the default quantity to 1.    
    else:
                
        quantity = 1


    # Get the Product object corresponding to the provided product_id
    product = Product.objects.get(pk=product_id)

    # Create an instance of the Cart class (from the cart.py file)
    cart_instance = Cart(request)

    # Add the product to the cart with the specified quantity
    cart_instance.add(product, quantity)

    # Check if the HTTP request is of type GET.
    if request.method == 'GET':
        # If it's a GET request, redirect the user to the homepage ('/').
        return redirect('/')

    # Render the 'cart.html' template (this is where the cart content is expected to be displayed)
    return render(request, 'cart.html')


# Define the "delete_item" function that handles removing a product from the shopping cart.
# It receives the "request" parameter, which represents the received HTTP request.
# It also receives the "product_id" parameter, which is the ID of the product to be removed from the cart.
def delete_item(request, product_id):
    # Get the "Product" object corresponding to the ID received as a parameter.
    product = Product.objects.get(pk=product_id)

    # Create a "cart_instance" object from the "Cart" class and pass the "request" object as a parameter.
    cart_instance = Cart(request)

    # Call the "delete" method of the "cart_instance" object and pass the "Product" object as a parameter.
    # This method will remove the product from the shopping cart.
    cart_instance.delete(product)

    # Redirect the user to the cart page after removing the product.
    return render(request, 'cart.html')

    """except Product.DoesNotExist:
        # If the product does not exist, handle the error appropriately here (e.g., showing a message to the user).
        return render(request, 'error.html', {'message': 'The product does not exist'})"""


def clean_cart(request):
    # Create an instance of the 'Cart' class, passing the 'request' object as a parameter.
    cart_instance = Cart(request)

    # Use the 'clear()' method from the 'Cart' class to remove all products from the cart.
    cart_instance.clear()

    # Redirect the user to the store page after clearing the cart.
    return render(request, 'cart.html')



#TODO:1. create the models where we will store the information about the products offered by the restaurant (main, drinks..etc)

#TODO: 2. create the home page and render all the products in the page

#TODO: 3. Create a view called details.html to see the details of the products, in my case the details of the products are seen
# in the modal window

#TODO: 4. Create the cart in the nav bar

#TODO: when you press button ' the add to cart'  the products should be added to the cart

#TODO: 5. Create the Cart class to control the shopping cart (add to cart, delete items etc..)

#TODO: 6. Create the Cart views (add to cart, delete items etc..)





#TODO: DEBE HABER UNA PAGINA CON LOS DETALLES DE LA COMPRA QUE SE VA HACER
#TODO: CREAR USER SYSTEM

