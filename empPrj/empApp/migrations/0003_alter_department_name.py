# Generated by Django 3.2.8 on 2021-10-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0002_auto_20210918_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Department Name'),
        ),
    ]
