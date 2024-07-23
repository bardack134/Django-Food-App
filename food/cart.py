class Cart:
    def __init__(self, request):
        """
        Defines a class to manage the shopping cart.

        Args:
            request (HttpRequest): The current HTTP request, which contains the user's session.
        """
        
        self.request = request  # Stores the current request to access the session.
        
        
        # Stores the current user's session. This means we can store information about the user, such as their shopping cart 
        # or profile details, in a session variable, and that information will persist throughout the user's interaction with the website.
        self.session = request.session  


        # Try to get the shopping cart from the session.
        cart = self.session.get('cart')
        
        
        # Try to get the total amount to pay from the session.
        Total_to_pay = self.session.get('cartTotalToPay')
        
        
        if not cart:
            # in this line of code, we create an empty dictionary in the user session with the key 'cart',
            # and we store self.session['cart'] in a variable called cart
            cart = self.session['cart'] = {}
            
            
            # Initialize the total amount to '0', slef.session has now a key called "cartTotalToPay" with the calue of 0
            Total_to_pay = self.session['cartTotalToPay'] = '0'
        
        
        # We create the cart and we pass it as a constructor attribute
        self.cart = cart
        self.Total_to_pay = float(Total_to_pay)

    
    
    def add(self, product, quantity):
        """
        Function to add products to the cart. It takes two parameters: quantity and the product to add to the cart.
        """
        
        # Checks if the product’s ID is not already a key in the self.cart dictionary.
        if str(product.id) not in self.cart.keys():


            # If the product's ID is not in the self.cart dictionary, it means the product has not been added to the cart before.
            # In this case, add the product to the cart as a new dictionary with the following information:
            self.cart[product.id] = {
                
                "product_id": product.id,             
                'type': product.product_type,             
                "name": product.item_name ,                  
                "quantity": quantity,                    
                "price": str(product.item_price),           
                "image": product.imagen.url,          
                "subtotal": str(quantity * product.item_price),  # We calculate the subtotal
            }
        
        
        # If the product is already in the cart, update the product's information.            
        else:
            
            # Iterates over the items in the cart to find the matching product ID.
            for key, value in self.cart.items():

                # check if the dictionary key matches the ID of the product
                if key == str(product.id):


                    # Updates the quantity and subtotal for the existing product in the cart.
                    value["quantity"] = str(int(value["quantity"]) + quantity)


                    # Calculate the new subtotal with the updated quantity and the product's price.
                    value["subtotal"] = str(float(value["quantity"]) * float(value["price"]))


                    # Break the loop as we have found the product in the cart and updated the quantity.
                    break


        # Call the save() method to save the changes to the session.
        self.save()
       
        print()
        print("Product added successfully")
        print()

        
    def save(self):
        """
        Save changes to the shopping cart
        """
        
        # track the total amount of the cart.
        Total_to_pay = 0


        # Iterate through the items in the cart, where 'key' is the product id and 'value' is a dictionary with product details.
        for key, value in self.cart.items():

            # Add the subtotal of the current product to the total amount.
            Total_to_pay += float(value["subtotal"])


        # Save the total amount in the session variable for later use.
        self.session['cartTotalToPay'] = Total_to_pay


        # Saves the updated cart dictionary to the session under the key 'cart'. 
        # This ensures that the cart data is preserved between HTTP requests and is accessible in future interactions.
        self.session['cart'] = self.cart


        # Indicate that the session has been modified to ensure that changes are saved correctly.
        # This setting is necessary for Django to know that changes have been made to the session. 
        self.session.modified = True

    
    def delete(self, product):
        """
        This function is responsible for removing a specific product from the shopping cart.
        """

        # product.id are stored the self.cart dictionary as string.
        product_id = str(product.id)


        # Check if the product ID is present as a key in the self.cart dictionary. 
        if product_id in self.cart:

            # the product is in the cart, remove it using the `del` statement.
            del self.cart[product_id]


            # Save changes to the session after removing the product.
            self.save()



    def subtract_products(self, product):
        
        # Loop through all the key-value pairs in the self.carro dictionary.
        for key, value in self.carro.items():

            #key is the product ID, and value is a dictionary containing details about the product.
            if key == str(product.id):


                # Decreases the quantity of the product by 1. This updates the value  "quantity"  in the product's dictionary within self.cart.
                value["quantity"] = value["quantity"] - 1


                # Recalculate the subtotal with the updated quantity and the product's price.
                value["subtotal"] = str(float(value["quantity"]) * float(value["price"]))


                # If the updated quantity is less than 1, remove the product from the cart.
                if value["quantity"] < 1:
                    self.delete(product)
                    
                    
                # Break the loop as we have found the product in the cart and updated the quantity.
                break


        # Save changes to the session after removing the product.
        self.save()
        


    def clear(self):
        """
        # This function is used to delete all products that are in the shopping cart.
        """
        
        # Empty the 'self.cart' dictionary by assigning an empty dictionary.
        self.session['cart'] = {}
        
        
        # Set the total amount to "0" in the session to indicate that the cart is now empty.
        self.session['cartTotalToPay'] = "0"
        
        
        self.session.modified = True







