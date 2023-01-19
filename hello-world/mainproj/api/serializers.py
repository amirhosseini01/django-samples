from rest_framework import serializers
from firstapp.models import FirstApp

class FirstAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstApp
        fields = '__all__'
