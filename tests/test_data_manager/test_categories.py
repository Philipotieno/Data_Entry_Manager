import pytest
from faker import Faker
from django.urls import reverse
from mixer.backend.django import mixer
from data_manager.models import Category, CategoryDetails
from data_manager.serializers import CategorySerializer
from data_manager.views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView


@pytest.fixture
def fake():
    """Create a Faker instance."""
    return Faker()

@pytest.fixture
def category():
    """Create a Category object using the mixer."""    
    return mixer.blend(Category)

@pytest.fixture
def category_details(category):
    """Create a CategoryDetails object using the mixer."""
    return mixer.blend(CategoryDetails, category=category)

# @pytest.mark.django_db
# def test_create_category(api_client, fake):
#     """Test the creation of a category."""
#     url = reverse('category-list-create')
#     category_name = fake.word()
#     description = fake.text()

#     data = {
#         'category_name': category_name,
#         'description': description
#     }

#     request = api_client.post(url, data, format='json')
#     response = CategoryListCreateAPIView.as_view()(request)

#     assert response.status_code == 201
#     assert Category.objects.count() == 1

#     category = Category.objects.first()
#     assert category.category_name == category_name
#     assert category.description == description

#     serializer = CategorySerializer(category)
#     assert response.data == serializer.data


@pytest.mark.django_db
def test_category_list(api_client):
    """Test listing of all categories."""
    url = reverse('category-list-create')

    # Create additional categories for testing
    for _ in range(3):
        mixer.blend(Category)
    
    request = api_client.get(url)
    response = CategoryListCreateAPIView.as_view()(request)

    assert response.status_code == 200
    assert len(response.data) == Category.objects.count()

@pytest.mark.django_db
def test_category_list_with_filter(api_client, fake):
    """Test the category list endpoint with category_name filter."""
    url = reverse('category-list-create')
    category_name = fake.word()

    # Create categories with different names for testing
    for _ in range(3):
        mixer.blend(Category)

    # Create a category with the specified category_name
    category_with_filter = mixer.blend(Category, category_name=category_name)

    request = api_client.get(url, {'category_name': category_name})
    response = CategoryListCreateAPIView.as_view()(request)

    # import pdb ; pdb.set_trace()

    assert response.status_code == 200
    assert len(response.data) == 1

    category_data = response.data[0]['category'][0]
    assert category_data['category_name'] == category_name



@pytest.mark.django_db
def test_category_retrieve(api_client, category):
    """Test the listing of a single category."""
    url = reverse('category-retrieve-update-destroy', kwargs={'pk': category.pk})

    request = api_client.get(url)
    response = CategoryRetrieveUpdateDestroyAPIView.as_view()(request, pk=category.pk)


    assert response.status_code == 200
    assert response.data['category']['category_name'] == category.category_name
    assert len(response.data) == 2
    assert response.data['category']['id'] == category.id
    # assert response.data['category_details'][0]['name'] == category_details.name
    # assert response.data['category_details'][0]['value'] == category_details.value
