# Generated by Django 5.0.2 on 2024-02-19 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_about_about_long_desc_alter_blogs_create_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='About_Image',
            new_name='Abou_Image',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='About_Long_Desc',
            new_name='Abou_Long_Desc',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='About_Title',
            new_name='Abou_Title',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='Create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 19, 11, 15, 51, 512981)),
        ),
    ]
