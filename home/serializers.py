from rest_framework import serializers


class PosterSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=100)
    short_description=serializers.CharField(max_length=300)
    url_title=serializers.CharField(max_length=50)
    url=serializers.CharField(max_length=100)
    image=serializers.ImageField(required=False)
    is_active=serializers.BooleanField()
    created_date=serializers.DateTimeField()