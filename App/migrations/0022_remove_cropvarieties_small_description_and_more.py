# Generated by Django 4.2.3 on 2023-08-29 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0021_crop_disease_disease_controls_disease_symptoms_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropvarieties',
            name='small_description',
        ),
        migrations.RemoveField(
            model_name='varieties',
            name='small_description',
        ),
    ]
