# Generated by Django 5.1.3 on 2024-12-07 03:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_project_images_projectimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimages',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.project'),
        ),
    ]
