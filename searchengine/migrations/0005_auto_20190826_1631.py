# Generated by Django 2.2.4 on 2019-08-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0004_auto_20190826_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_model',
            name='Reservation_ticket',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
