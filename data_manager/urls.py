from django.urls import include, path
from rest_framework import routers
from .views import CategoryListCreateView, CategoryDetailsViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryListCreateView)

urlpatterns = [
    path('', include(router.urls)),
    path('category_details/', CategoryDetailsViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-details-list'),
    # path('category_details/<int:pk>/', CategoryDetailsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='category-details-detail'),
]