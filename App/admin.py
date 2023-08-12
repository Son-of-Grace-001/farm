from django.contrib import admin

# Register your models here.
from . models import Category, Varieties
from . models import Disease, CropVarieties
from . models import ProductCategory, ProductVarieties
from . models import Symptoms, CropCategory, Crop_Disease
admin.site.register(Category)
admin.site.register(CropCategory)
admin.site.register(ProductCategory)
admin.site.register(ProductVarieties)


class MyVariety(admin.ModelAdmin):
    list_display = ('category_var', 'name', 'date', 'small_description',
                    'weather', 'yields', 'category', 'image')

admin.site.register(Varieties, MyVariety)

class MyCropVariety(admin.ModelAdmin):
    list_display = ('category_var', 'name', 'date', 'small_description',
                    'weather', 'yields', 'category', 'image')

admin.site.register(CropVarieties, MyCropVariety)

class MyDiseases(admin.ModelAdmin):
    list_display = ('name', 'date', 'disease_description', 'symptoms', 'control', 'varieties')
admin.site.register(Disease, MyDiseases)

class MyC_Diseases(admin.ModelAdmin):
    list_display = ('name', 'date', 'disease_description', 'symptoms', 'control', 'varieties')
admin.site.register(Crop_Disease, MyC_Diseases)
