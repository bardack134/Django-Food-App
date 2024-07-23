from django.db import models


  # Main Food item model 
class Item(models.Model):
    
    # item caracterictics (name, description, price, imagen)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField( max_digits = 5, decimal_places=2)
    imagen = models.ImageField(upload_to='food', null=True, blank=True)
    
    product_type=models.CharField(max_length=200, default='itemx', editable=False)
       
    # Date and time when item was created 
    created_at = models.DateTimeField(auto_now_add=True)  
    
    # Date and time when item was last updated
    updated_at = models.DateTimeField(auto_now=True)  
    
    # String representation of the model, returns item name
    def __str__(self):
        return self.item_name
      

# Drinks items models
class DrinksItems(models.Model):
    
    # item caracterictics (name, description, price, imagen)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField( max_digits = 5, decimal_places=2)
    imagen = models.ImageField(upload_to='food', null=True, blank=True)
    
    product_type=models.CharField(max_length=200, default='drinks', editable=False)
    
    # Date and time when item was created 
    created_at = models.DateTimeField(auto_now_add=True)  
    
    # Date and time when item was last updated
    updated_at = models.DateTimeField(auto_now=True)  
    
    # String representation of the model, returns item name
    def __str__(self):
        return self.item_name
      
      
# Desserts items models
class DessertsItems(models.Model):
    
    # item caracterictics (name, description, price, imagen)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField( max_digits = 5, decimal_places=2)
    imagen = models.ImageField(upload_to='food', null=True, blank=True)
    
    product_type=models.CharField(max_length=200, default='desserts', editable=False)
    
    # Date and time when item was created 
    created_at = models.DateTimeField(auto_now_add=True)  
    
    # Date and time when item was last updated
    updated_at = models.DateTimeField(auto_now=True)  
    
    # String representation of the model, returns item name
    def __str__(self):
        return self.item_name
      

# Sides items models
class SidesItems(models.Model):
    
    # item caracterictics (name, description, price, imagen)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField( max_digits = 5, decimal_places=2)
    imagen = models.ImageField(upload_to='food', null=True, blank=True)
    
    product_type=models.CharField(max_length=200, default='sides', editable=False)
    
    # Date and time when item was created 
    created_at = models.DateTimeField(auto_now_add=True)  
    
    # Date and time when item was last updated
    updated_at = models.DateTimeField(auto_now=True)  
    
    # String representation of the model, returns item name
    def __str__(self):
        return self.item_name