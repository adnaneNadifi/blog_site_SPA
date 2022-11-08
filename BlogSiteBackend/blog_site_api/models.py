from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
        
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
