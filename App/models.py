from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category/")

    def __str__(self):
        return self.name
    

class Varieties(models.Model):
    category_var = models.CharField(max_length=100, default='chicken')
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    small_description = models.CharField(max_length=200)
    description = models.TextField()
    weather = models.CharField(max_length=200)
    yields = models.TextField()
    image =models.ImageField(upload_to ="varieties/" )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
      return self.name


class Disease(models.Model):
    name = models.CharField(max_length=100)
    pest_description = models.TextField( default='i')
    date = models.DateTimeField(auto_now_add=True)
    varieties = models.ForeignKey(Varieties, on_delete=models.CASCADE)
    def __str__(self):
      return self.name


class Symptoms(models.Model):
    sym = models.TextField()
    treatment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name="dis")

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="category/")

    def __str__(self):
        return self.name
    

class ProductVarieties(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    small_description = models.CharField(max_length=200)
    description = models.TextField()
    price  = models.CharField(max_length=100)
    image =models.ImageField(upload_to ="varieties/" )
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
      return self.name


class CropCategory(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category/")

    def __str__(self):
        return self.name
    
class CropVarieties(models.Model):
    category_var = models.CharField(max_length=100, default='chicken')
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    small_description = models.CharField(max_length=200)
    description = models.TextField()
    weather = models.TextField()
    yields = models.TextField()
    image =models.ImageField(upload_to ="varieties/" )
    category = models.ForeignKey(CropCategory, on_delete=models.CASCADE)

    def __str__(self):
      return self.name