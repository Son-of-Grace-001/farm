# Generated by Django 4.2.3 on 2023-07-25 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_alter_productvarieties_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varieties',
            name='weather',
            field=models.TextField(),
        ),
    ]
