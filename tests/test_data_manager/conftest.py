# import pytest
# from django.conf import settings
# from model_bakery import baker
# from rest_framework.test import APIClient


# def pytest_configure():
#     settings.DEBUG = False
#     settings.configure()

# # def unfilled_category_bakery():
# #     def unfilled_category_bakery_batch(n):
# #         unfilled = baker.make(
# #             'category.Category',
# #             _fill_optional=[
# #                 'category_name',
# #                 'description'
# #             ],
# #         )
# #         return unfilled
# #     return unfilled_category_bakery_batch

# # @pytest.fixture
# # def filled_category_bakery():
# #     def filled_category_bakery_batch(n):
# #         filled = baker.make(
# #             'category.Category',
# #         )
# #         return filled
# #     return filled_category_bakery_batch

# # @pytest.fixture
# # def filled_category_details_bakery():
# #     def filled_category_details_bakery_batch():
# #         filled = baker.make(
# #             'category_details.CategoryDetails',
# #             category=baker.make('category.CategoryDetails'),   
# #         )
# #         return filled
# #     return filled_category_details_bakery_batch

# @pytest.fixture
# def api_client():
#     return APIClient
