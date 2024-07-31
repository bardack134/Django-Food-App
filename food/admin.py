from django.contrib import admin
from .models import  Category, Items

# Customizes the admin interface for the Item model
class ItemAdmin(admin.ModelAdmin):  
    
    # Display fields in the admin view
    list_display = ("item_name", "item_description", "item_price", "product_type")  
    
    # Makes created_at and updated_at read-only
    readonly_fields = ('created_at', 'updated_at')  
    

class CategoryAdmin(admin.ModelAdmin):

    #estos campos habiamos determinado que se actualizarian automaticamente, por lo tanto seran solo Lectura 
	readonly_fields=('created', 'updated')
	
 

# Registers the models with the custom admin interfaces
admin.site.register(Items, ItemAdmin) 

admin.site.register(Category, CategoryAdmin)