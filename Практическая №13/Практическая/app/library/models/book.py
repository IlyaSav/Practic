from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')
    image = models.ImageField(upload_to='book/%Y/%m%d', default='default_image.jpg')

    def __str__(self):
        return self.title