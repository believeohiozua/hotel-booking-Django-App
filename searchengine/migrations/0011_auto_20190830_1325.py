# Generated by Django 2.2.4 on 2019-08-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0010_auto_20190827_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_model',
            name='Room_pop',
            field=models.ManyToManyField(blank=True, default='1', to='searchengine.Population'),
        ),
    ]