from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.IntegerField()


    def __str__(self):
        return f"{self.title} by {self.author} Published in {self.published_date}"

# Create your models here.
