from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
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
    
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

def create_superuser(self, email, password=None, **extra_fields):
      extra_fields.setdefault("is_staff", True)
      extra_fields.setdefault("is_superuser", True)

      if extra_fields.get("is_staff") is not True:
          raise ValueError("Superuser must have is_staff=True.")
      if extra_fields.get("is_superuser") is not True:
          raise ValueError("Superuser must have is_superuser=True.")

      return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    username = models.CharField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "password"]

    def __str__(self):
        return self.email