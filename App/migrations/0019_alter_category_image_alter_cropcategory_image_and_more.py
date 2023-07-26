# Generated by Django 4.2.3 on 2023-07-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0018_alter_varieties_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='cropcategory',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='cropvarieties',
            name='category_var',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cropvarieties',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='disease',
            name='pest_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='productvarieties',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='varieties',
            name='category_var',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='varieties',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]