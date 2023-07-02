from rest_framework import viewsets, status
from .models import Category, CategoryDetails
from .serializers import CategorySerializer, CategoryDetailsSerializer
from rest_framework.response import Response
from rest_framework import generics



class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# class CategoryListCreateView(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=201, headers=headers)

class CategoryDetailsViewSet(viewsets.ModelViewSet):
    pass
#     serializer_class = CategoryDetailsSerializer

#     def get_queryset(self):
#         category_id = self.request.query_params.get('category_id')
#         if category_id:
#             queryset = CategoryDetails.objects.filter(category_id=category_id)
#         else:
#             queryset = CategoryDetails.objects.all()
#         return queryset

#     def create(self, request, *args, **kwargs):
#         category_id = request.query_params.get('category_id')
#         try:
#             category = Category.objects.get(id=category_id)
#         except Category.DoesNotExist:
#             return Response({'error': 'Category not found.'}, status=status.HTTP_404_NOT_FOUND)

#         request.data['category'] = category_id
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)