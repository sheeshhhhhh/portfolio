# Generated by Django 5.1.3 on 2024-12-08 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_project_website_link_alter_projectimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimages',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
