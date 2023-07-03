from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_name = models.CharField(max_length=250, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.category_name
    

class CategoryDetails(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.category.category_name} - Details"
