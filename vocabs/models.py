from django.db import models
from django.contrib.auth.models import User
class english_vocabs(models.Model):
    vocab=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    cat=models.ManyToManyField("category_languages",blank=True,null=True)


    def __str__(self):
        return self.vocab

class category_languages(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name