from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pages = models.IntegerField()

    def __str__(self):
        return f"{self.author}, {self.title}, {self.pages} pagini (db_index:{self.pk})"