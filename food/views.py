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


def get_product_type(product_type, product_id): 
    """
    This function determine what type of model the product belongs to and obtain the product information.
    """
    
    model_type={
        
        'itemx':Item,
        'drinks':DrinksItems,
        'desserts':DessertsItems,
        'sides':SidesItems,
       
    }
    
    
    # from model_type 'dictionary' get the model type to which the product belongs
    model=model_type.get(product_type)
    
    
    if model is not None:
        
        return get_object_or_404(model, pk=product_id)
    
    return None
    
    

def cart(request):
    """
    View to display the shopping cart
    """
    
    return render(request, 'cart.html')



def add_item(request, product_id, product_type):
    """
    Add a Product to Cart
    """
    
    if request.method == 'POST':
        
        # Get the quantity of the product from the form and convert it to an integer.
        quantity = int(request.POST['quantity'])
    
    # If is a GET request, set the default quantity to 1.    
    else:
                
        quantity = 1


    # obtain the product
    product = get_product_type(product_type, product_id)
    
    
    # Create an instance of the Cart class (from the cart.py file)
    cart_instance = Cart(request)


    # Add the product to the cart with the specified quantity
    cart_instance.add(product, quantity)


    if request.method == 'GET':
        
        # redirect the user to the homepage ('/').
        return redirect('/')

    
    # Redirect to the homepage after adding the product
    return redirect('food:home')



def delete_item(request, product_id, product_type):
    """
    # This function remove a product from the shopping cart.
    """
    
    # obtain the product
    product = get_product_type(product_type, product_id)


    # Create a "cart_instance" object from the "Cart" class and pass the "request" object as a parameter.
    cart_instance = Cart(request)


    # Call the "delete" method of the "cart_instance" object and pass the "Product" object as a parameter.
    cart_instance.delete(product)


    # Redirect to the home page after removing the product.
    return redirect('food:home')

    

def clean_cart(request):
    
    # Create an instance of the 'Cart' class, passing the 'request' object as a parameter.
    cart_instance = Cart(request)


    # Use the 'clear()' method from the 'Cart' class to remove all products from the cart.
    cart_instance.clear()


    # Redirect the user to the store page after clearing the cart.
    return render(request, 'cart.html')



"""STEPS I DID TO CREATE THE PROYECT """


#TODO:1. create the models where we will store the information about the products offered by the restaurant (main, drinks..etc)


#TODO: 2. create the home page and render all the products in the page


#TODO: 3. Create a view called details.html to see the details of the products, in my case the details of the products are seen
# in the modal window


#TODO: 4. Create the cart in the nav bar


#TODO: when you press button ' the add to cart'  the products should be added to the cart


#TODO: 5. Create the Cart class 'cart.py' to control the shopping cart (add to cart, delete items etc..)


#TODO: 6. Create the Cart views (add to cart, delete items etc..)


#TODO: 7. Since I have 4 models, I create a separate function to determine what type of model the product belongs to.


#TODO: 8. Create the add_item url


#TODO: 9. In the modal window 'index.html', i pass the url 'food:add_item' with the neccessary parameters for our 'add_item view'


#TODO: 10. Create the url for the 'delete_item view'



#TODO: DEBE HABER UNA PAGINA CON LOS DETALLES DE LA COMPRA QUE SE VA HACER
#TODO: CREAR USER SYSTEM

