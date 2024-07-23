from django.urls import path

from . import views

app_name='food'
urlpatterns = [
    
    #home　page url
    path("", views.home, name="home"),
    
    path("item/", views.item, name="item"),
    
    path("details/<int:item_id>", views.detail, name="detail"),
    
    # url to add a new item to the cart
    path("add_item/<int:product_id>/<str:product_type>", views.add_item, name="add_item"),
    
    # url for 'delete_item view'
    path("delete_item/<int:product_id>/<str:product_type>", views.delete_item, name="delete_item"),
    
    
]