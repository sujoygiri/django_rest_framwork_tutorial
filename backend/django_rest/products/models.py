from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2,default=99.99)

    @property
    def salePrice(self):
        return "%.2f" %(float(self.price) * 0.8)

    def __str__(self):
        return self.title