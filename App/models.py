from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
    

class Varieties(models.Model):
    category_var = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    weather = models.TextField()
    yields = models.TextField()
    image =models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
      return self.name


class Disease(models.Model):
    name = models.CharField(max_length=100)
    pest_description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    varieties = models.ForeignKey(Varieties, on_delete=models.CASCADE)
    def __str__(self):
      return self.name

class Symptom(models.Model):
    disease_sym = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    def __str__(self):
      return self.name

class Control(models.Model):
    disease_con = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    disease = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    def __str__(self):
      return self.name
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
    

class ProductVarieties(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    small_description = models.CharField(max_length=200)
    description = models.TextField()
    price  = models.CharField(max_length=100)
    image =models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
      return self.name


class CropCategory(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
    
class CropVarieties(models.Model):
    category_var = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    weather = models.TextField()
    yields = models.TextField()
    image =models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(CropCategory, on_delete=models.CASCADE)

    def __str__(self):
      return self.name
    
class Crop_Disease(models.Model):
    name = models.CharField(max_length=100)
    disease_description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    varieties = models.ForeignKey(Varieties, on_delete=models.CASCADE)
    symptoms = models.TextField()
    controls = models.TextField()
    def __str__(self):
      return self.name