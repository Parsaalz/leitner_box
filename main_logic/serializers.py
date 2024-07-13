from rest_framework import serializers

class OrderSerializer(serializers.Serializer):
    user=serializers.CharField(max_length=100)
    payment_date=serializers.DateTimeField()
    is_paid=serializers.BooleanField()
    is_delete=serializers.BooleanField()