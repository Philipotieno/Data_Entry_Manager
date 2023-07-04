import pytest
from rest_framework.test import APIRequestFactory

@pytest.fixture
def api_client():
    """Create a DRF API client using APIRequestFactory."""
    return APIRequestFactory()

