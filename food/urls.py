from django.urls import path

from . import views

app_name='food'
urlpatterns = [
    
    #home　page url. show all products
    path("", views.home, name="home"),
        
    # url to add a new item to the cart
    path("add_item/<int:product_id>/<str:product_type>", views.add_item, name="add_item"),
    
    # url for 'delete_item view'
    path("delete_item/<int:product_id>/<str:product_type>", views.delete_item, name="delete_item"),
    
    #search a product acording to its category
    path('ProductsByCategory/<int:category_id>', views.home, name='ProductsByCategory'),
    
]