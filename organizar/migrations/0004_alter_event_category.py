# Generated by Django 5.1.5 on 2025-01-25 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizar', '0003_alter_category_description_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='organizar.category'),
        ),
    ]
