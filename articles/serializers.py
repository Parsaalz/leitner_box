from rest_framework import serializers
from .models import Category_Articles
class ArticlesSerializers(serializers.Serializer):
    title=serializers.CharField(max_length=100)
    short_description=serializers.CharField(max_length=500)
    description=serializers.CharField(max_length=500)
    image=serializers.ImageField()
    author_name=serializers.CharField(max_length=100)
    category=serializers.PrimaryKeyRelatedField(queryset=Category_Articles.objects.all(),many=True)
    published=serializers.CharField()
    created_date=serializers.DateTimeField(required=False)