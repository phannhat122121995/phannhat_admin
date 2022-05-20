# Generated by Django 3.2.13 on 2022-05-07 08:05

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_index', '0007_delete_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
