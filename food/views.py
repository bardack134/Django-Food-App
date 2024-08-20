from django.http import HttpResponse
from django.shortcuts import redirect, render

from food.form import UserForm
from foodApp import settings
from .models import  Category, Items
from django.shortcuts import get_object_or_404, render
from twilio.rest import Client
# Create your views here.
    
def home(request, category_id=None):
    """
    This view provides all products or products according to their category
    """
    
    # products according to their category if the category_id is provided
    if category_id:
        
        # Get the Category object that matches the provided category_id
        objCategory = Category.objects.get(id=category_id)


        # get all products associated with the category gotten before
        product_list = objCategory.products.all()


        # Get all categories to display in the sidebar or menu
        category_list = Category.objects.all()


        # Prepare the context dictionary with category_list and product_list
        context = {
            'category_list': category_list,  
            'product_list': product_list,   
        }


    # category_id is optional so if it is not provided we render all the existing products in the database
    else:
        
        # Get all categories
        category_list = Category.objects.all()

        # Get all products in the database
        item_list = Items.objects.all()

        # Prepare the context dictionary with category_list and item_list
        context = {
            "product_list": item_list,     
            "category_list": category_list, 
        }

    # Render the 'food/example.html' template with the prepared context
    return render(request, 'food/index.html', context)


def user_data(request):
    """
    view that corresponds to where the user enters their data for shipping
    """
    if request.method == 'POST':
        
        # form with user data
        form=UserForm(request.POST)
        
        if form.is_valid():
            
            # We save the data in the session
            request.session['personal_data'] = form.cleaned_data
            
            # Redirects to the confirmation page
            return redirect('food:confirmation')
            
    else:        
      
        form=UserForm()
    
        context = {
                "form": form,     
                }
    
        return render(request, 'food/userData.html', context)    
    
    
def confirmation(request):
    """
    This view is the confirmation page, show  the user's details and the products they are purchasing.
    """
    # user data is saved in the session
    personal_data = request.session.get('personal_data')
    
    context = {
                'personal_data': personal_data,    
                }    
        
    return render(request, 'food/confirmation.html', context)
    
    
def thanks(request):    
    """
    This view sends the information thatorder was made while sending the data to the restaurant.
    """
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    
    client = Client(account_sid, auth_token)

    personal_data = request.session.get('personal_data')
    
    cart=request.session.get('cart')
    
    # user data
    name=personal_data['name']
    phonenumber=personal_data['phonenumber']
    address=personal_data['address']
    
    items_list=[]
    
    for key, value in cart.items():
        item_name=value['name']
        item_price=value['price']
        item_quantity=value['quantity']
        items_list.append(f'{item_name} - ${item_price} - {item_quantity}')
    
    items_string='\n'.join(items_list)    
    
    message = client.messages.create(
        body=f"name={name}\n phonenumber={phonenumber}\n address={address}\n products={items_string} \n total=${request.session['cartTotalToPay']} ",
        from_="+12564620138",
        to="+8107045317684",
    )

    clean_cart(request)
    
    return render(request, 'food/thanks.html')
    
                  
"""VIEWS FOR THE SHOPPING CART"""
from .cart import Cart

def cart(request):
    """
    View to display the shopping cart
    """
    
    return render(request, 'food/cart.html')



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

    print(f'you sent a product with the following id {product_id}')
    
    # obtain the product
    product =  get_object_or_404(Items, id=product_id)
    
    
    # Create an instance of the Cart class (from the cart.py file)
    cart_instance = Cart(request)


    # Add the product to the cart with the specified quantity
    cart_instance.add(product, quantity)


    if request.method == 'GET':
        
        # redirect the user to the homepage ('/').
        return redirect('/')

    
    # Redirect the user to the same page where he made the request
    # more infor in https://docs.djangoproject.com/en/5.0/ref/request-response/
    return redirect(request.META.get('HTTP_REFERER'))



def delete_item(request, product_id):
    """
    # This function remove a product from the shopping cart.
    """
    
    # obtain the product
    product = get_object_or_404(Items, id=product_id)


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


    # Redirect the user to the same page where he made the request
    # more infor in https://docs.djangoproject.com/en/5.0/ref/request-response/
    return redirect(request.META.get('HTTP_REFERER'))


