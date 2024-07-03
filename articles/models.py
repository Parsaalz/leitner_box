from django.db import models
from django.contrib.auth.models import User
import datetime
choices_custom={
    "d":"draft",
    "p":"published",
}
class Articles_page(models.Model):
    title=models.CharField(max_length=100,default="")
    short_description=models.TextField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/images/')
    author_name=models.CharField(max_length=100)
    category=models.ManyToManyField("Category_Articles",blank=True,null=True)
    published=models.CharField(max_length=100,choices=choices_custom,default="p")
    created_date=models.DateTimeField(default=datetime.datetime.today)
    def __str__(self):
        return self.title
    

class Category_Articles(models.Model):
    name=models.CharField(max_length=100)
    published=models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class ArticlesComment(models.Model):
    article=models.ForeignKey(Articles_page,on_delete=models.CASCADE,verbose_name="مقاله")
    parent=models.ForeignKey('ArticlesComment',on_delete=models.CASCADE,verbose_name="والد",null=True,blank=True)
    text=models.TextField(verbose_name="متن")
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")   
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="زمان ساخت")

    class Meta:
        verbose_name="کامنت مقاله"
        verbose_name_plural="کامنت مقالات"


    def __str__(self):
        return f'{self.user}'
