from django.db import models

choices_custom=[
    ("d","draft"),
    ("p","published"),
]
class Articles_page(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='media/images/')
    author_name=models.CharField(max_length=100)
    category=models.ManyToManyField("Category_Articles")
    published=models.CharField(max_length=100,choices=choices_custom,default="p")
    def __str__(self):
        return self.title
    

class Category_Articles(models.Model):
    name=models.CharField(max_length=100)
    published=models.BooleanField(default=True)
    def __str__(self):
        return self.name
    