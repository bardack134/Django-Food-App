from django.contrib import admin
from .models import DessertsItems, DrinksItems, Item, SidesItems

# Customizes the admin interface for the Item model
class ItemAdmin(admin.ModelAdmin):  
    
    # Display fields in the admin view
    list_display = ("item_name", "item_description", "item_price")  
    
    # Makes created_at and updated_at read-only
    readonly_fields = ('created_at', 'updated_at')  
    
    
# Customizes the admin interface for the DrinksItems
class DrinksItemsAdmin(admin.ModelAdmin):  
    
    # Display fields in the admin view
    list_display = ("item_name", "item_description", "item_price")  
    
    # Makes created_at and updated_at read-only
    readonly_fields = ('created_at', 'updated_at')  
    
    
# Customizes the admin interface for the DessertsItems model
class DessertsItemsAdmin(admin.ModelAdmin):  
    
    # Display fields in the admin view
    list_display = ("item_name", "item_description", "item_price")  
    
    # Makes created_at and updated_at read-only
    readonly_fields = ('created_at', 'updated_at')  
    
    
# Customizes the admin interface for the Item model
class SidesItemsAdmin(admin.ModelAdmin):  
    
    # Display fields in the admin view
    list_display = ("item_name", "item_description", "item_price")  
    
    # Makes created_at and updated_at read-only
    readonly_fields = ('created_at', 'updated_at')  


# Registers the models with the custom admin interfaces
admin.site.register(Item, ItemAdmin) 
admin.site.register(DrinksItems, DrinksItemsAdmin) 
admin.site.register(DessertsItems, DessertsItemsAdmin) 
admin.site.register(SidesItems, SidesItemsAdmin) 
