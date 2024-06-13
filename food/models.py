from django.db import models



class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.DecimalField( max_digits = 5, decimal_places=2)
    imagen = models.ImageField(upload_to='food', null=True, blank=True)
    def __str__(self):
        return self.item_name