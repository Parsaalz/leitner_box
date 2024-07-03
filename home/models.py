from django.db import models

class Poster(models.Model):
    title=models.CharField(max_length=100,verbose_name="عنوان")
    short_description=models.TextField(max_length=300,verbose_name='توضیحات کوتاه')
    url_title=models.CharField(max_length=50)
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to='poster/')
    is_active=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="پوستر"
        verbose_name_plural="پوستر ها"

class CustomerClub(models.Model):
    email=models.CharField(max_length=100)


    class Meta:
        verbose_name="باشگاه مشتری"
        verbose_name_plural="باشگاه مشتریان"


    def __str__(self):
        return self.email
