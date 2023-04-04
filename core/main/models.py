from django.db import models

class Prodcut(models.Model):
    name = models.CharField("Name", max_length = 50)
    price = models.PositiveBigIntegerField("Price")
    
    def __str__(self):
        return f"{self.name} || {self.price}"
