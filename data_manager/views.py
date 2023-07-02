from rest_framework import viewsets, status
from .models import Category, CategoryDetails
from .serializers import CategorySerializer, CategoryDetailsSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import NotFound



class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)
        data = []
        for category in categories:
            category_details = CategoryDetails.objects.filter(category=category)
            details_serializer = CategoryDetailsSerializer(category_details, many=True)
            category_data = {
                'category': serializer.data,
                'category_details': details_serializer.data
            }
            data.append(category_data)
        return Response(data)

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        category_details = CategoryDetails.objects.filter(category=instance)
        details_serializer = CategoryDetailsSerializer(category_details, many=True)
        data = {
            'category': serializer.data,
            'category_details': details_serializer.data
        }
        return Response(data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CategoryDetailsCreateAPIView(generics.CreateAPIView):
    queryset = CategoryDetails.objects.all()
    serializer_class = CategoryDetailsSerializer

    def get_category(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise NotFound(detail="Category not found.")

    def perform_create(self, serializer):
        category_id = self.kwargs['category_id']
        category = self.get_category(category_id)
        serializer.save(category=category)