from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import  Category, Items
from django.shortcuts import get_object_or_404, render

# Create your views here.
def home(request):
    
    category_list = Category.objects.all()
    
    item_list = Items.objects.all()
    
    context = {
        
        "item_list": item_list,
        
        "category_list": category_list,
       
    }
    

    return render(request, "food/example.html", context)
    # return render(request, "food/index.html", context)
    


def ProductsByCategory(request, category_id):
   
    objCategory = Category.objects.get(id=category_id)

    
    product_list = objCategory.products.all()

    
    category_list = Category.objects.all()

   
    context = {
        'category_list': category_list, 
        'product_list': product_list,  
    }

    
    return render(request, 'food/example.html', context)







"""VIEWS FOR THE SHOPPING CART"""
from .cart import Cart


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

    print(product_type, product_id)
    
    # obtain the product
    product =  get_object_or_404(product_type, product_id)
    
    
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


#TODO:1. create the model where we will store the information about the products offered by the restaurant 


#TODO: 2. create the home page and render all the products in the page


#TODO: 3. the details of the product will be seen in a modal window


#TODO: 4. Create the cart in the nav bar


#TODO: when you press button ' the add to cart'  the products should be added to the cart


#TODO: 5. Create the Cart class 'cart.py' to control the shopping cart (add to cart, delete items etc..)


#TODO: 6. Create the Cart views (add to cart, delete items etc..)


#TODO: 7. Create the add_item url


#TODO: 8. (main menu) In the modal window 'index.html', i passed the url 'food:add_item' with the neccessary parameters for our 'add_item view'


#TODO: 9. Create the url for the 'delete_item view' and put it to work in the navbar cart


#TODO: 10.  until now, I have only used the add_view url with the main menu. I will now add it for drinks, desserts, and sides.





