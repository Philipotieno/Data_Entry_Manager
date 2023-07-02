from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class CategoryDetails(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    employees = models.IntegerField()


    def __str__(self):
        return f"{self.category.name} - Details"