from rest_framework import serializers
from .models import Category, CategoryDetails


class CategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDetails
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    details = CategoryDetailsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'details')