from django.urls import path
from .views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, CategoryDetailsCreateAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
    path('category_details/<int:category_id>/', CategoryDetailsCreateAPIView.as_view(), name='category-details'),
]
