# Generated by Django 5.0.2 on 2024-02-15 11:06

import app.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_blogs_create_at_alter_blogs_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='tag',
            field=models.CharField(default='', max_length=300, null=True, verbose_name=app.models.Tags),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='Create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 15, 16, 36, 36, 780416)),
        ),
    ]
