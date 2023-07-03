from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.category_name
    

class CategoryDetails(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.category.category_name} - Details"
