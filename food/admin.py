from django.contrib import admin
from .models import Item

# Customizes the admin interface for the Item model
class ItemAdmin(admin.ModelAdmin):  
    
    # Display fields in the admin view
    list_display = ("item_name", "item_description", "item_price")  
    
    # Makes created_at and updated_at read-only
    readonly_fields = ('created_at', 'updated_at')  


# Registers the Item model with the custom admin interface
admin.site.register(Item, ItemAdmin) 
