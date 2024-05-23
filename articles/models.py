from django.db import models

class Articles_page(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='media/images/')
    author_name=models.CharField(max_length=100)
    category=models.ManyToManyField("Category_Articles")
    def __str__(self):
        return self.title
    

class Category_Articles(models.Model):
    name=models.CharField(max_length=100)