from django.db import models
from django.contrib.auth.models import User
class LitnerApp(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    level=models.SmallIntegerField(default=0)
    dl=models.DateField()
    word=models.CharField(max_length=100)
    answer=models.CharField(max_length=100,blank=True,null=True)
    show=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.word} {self.user}"
