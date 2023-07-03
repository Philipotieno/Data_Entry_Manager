from rest_framework import serializers
from .models import Category, CategoryDetails


class CategoryDetailsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    class Meta:
        model = CategoryDetails
        fields = ['name', 'value', 'created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    
    fields = CategoryDetailsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'description', 'created_at', 'updated_at', 'fields')


    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Category name is less than 3 characters")
        return value

    def validate_description(self, value):
        words = value.split()
        if len(words) < 2:
            raise serializers.ValidationError("Category description should contain more than one word.")
        return value