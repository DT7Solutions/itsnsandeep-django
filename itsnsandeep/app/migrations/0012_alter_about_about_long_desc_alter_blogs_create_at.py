# Generated by Django 5.0.2 on 2024-02-19 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_about_rename_description_portfolio_port_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='About_Long_Desc',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='Create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 19, 11, 9, 23, 525898)),
        ),
    ]