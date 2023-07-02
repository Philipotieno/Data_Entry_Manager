# from django.urls import include, path
# from rest_framework import routers
# from .views import CategoryListCreateAPIView, CategoryDetailsViewSet

# router = routers.DefaultRouter()
# router.register(r'category', CategoryListCreateAPIView)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('category_details/', CategoryDetailsViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-details-list'),
#     # path('category_details/<int:pk>/', CategoryDetailsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='category-details-detail'),
# ]

from django.urls import path
from .views import CategoryListCreateAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    # path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
]
