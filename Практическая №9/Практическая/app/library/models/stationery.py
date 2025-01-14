from django.db import models

class Stationery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='stationery/%Y/%m%d', default='default_image.jpg')