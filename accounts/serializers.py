from rest_framework import serializers


class AccountsSerializers(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    first_name=serializers.CharField(max_length=150)
    last_name=serializers.CharField(max_length=150)
    is_staff=serializers.BooleanField()