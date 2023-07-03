import pytest
from django.test import TestCase
from faker import Faker
from data_manager.models import Category, CategoryDetails

pytestmark = pytest.mark.django_db

@pytest.fixture
def faker():
    return Faker()

@pytestmark
def test_category_str(faker):
    category_name = faker.word()
    category = Category.objects.create(category_name=category_name, description=faker.text())
    assert str(category) == category_name

@pytestmark
def test_category_details_str(faker):
    category_name = faker.word()
    category = Category.objects.create(category_name=category_name, description=faker.text())
    category_details = CategoryDetails.objects.create(category=category, name=faker.word(), value=faker.word())
    expected_str = f"{category_name} - Details"
    assert str(category_details) == expected_str

@pytestmark
def test_category_creation(faker):
    category_name = faker.word()
    Category.objects.create(category_name=category_name, description=faker.text())
    assert Category.objects.count() == 1

@pytestmark
def test_category_details_creation(faker):
    category_name = faker.word()
    category = Category.objects.create(category_name=category_name, description=faker.text())
    CategoryDetails.objects.create(category=category, name=faker.word(), value=faker.word())
    assert CategoryDetails.objects.count() == 1
