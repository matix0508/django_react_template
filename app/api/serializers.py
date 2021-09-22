from rest_framework import serializers
from .models import FirstModel

class FirstModelSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FirstModel
        fields = ('id', 'field1', 'field2', 'field3')
        