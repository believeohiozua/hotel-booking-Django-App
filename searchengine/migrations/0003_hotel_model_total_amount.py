# Generated by Django 2.2.4 on 2019-08-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0002_auto_20190826_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel_model',
            name='Total_Amount',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]