from django.db import models



class Category(models.Model):
  
    name = models.CharField(max_length=200)

  
    created = models.DateTimeField(auto_now_add=True)

    
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = 'Category'  
        verbose_name_plural = 'Categories'  

   
    def __str__(self):
        return self.name



 
class Items(models.Model):
    
    product_type = models.ForeignKey(Category, on_delete=models.RESTRICT,  related_name='products')
    
    # item caracterictics (name, description, price, imagen)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField( max_digits = 5, decimal_places=2)
    imagen = models.ImageField(upload_to='food', null=True, blank=True)
    
      
    # Date and time when item was created 
    created_at = models.DateTimeField(auto_now_add=True)  
    
    # Date and time when item was last updated
    updated_at = models.DateTimeField(auto_now=True)  
    
    # String representation of the model, returns item name
    def __str__(self):
        return self.item_name
  