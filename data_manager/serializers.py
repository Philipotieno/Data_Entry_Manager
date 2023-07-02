from rest_framework import serializers
from .models import Category, CategoryDetails


class CategoryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDetails
        fields = ['name', 'value']

class CategorySerializer(serializers.ModelSerializer):
    fields = CategoryDetailsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'description', 'fields')


    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Category name is less than 3 characters")
        return value

    def validate_description(self, value):
        words = value.split()
        if len(words) < 2:
            raise serializers.ValidationError("Category description should contain more than one word.")
        return value