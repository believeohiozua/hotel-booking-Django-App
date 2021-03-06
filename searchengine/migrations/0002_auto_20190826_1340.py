# Generated by Django 2.2.4 on 2019-08-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='hotel_model',
            name='Room_type',
            field=models.CharField(choices=[('Single', 'Singles Rooms'), ('Double', 'Doubles Rooms'), ('Triple', 'Triples Rooms'), ('Quadruple', 'Quadruples Rooms')], default='Single', help_text='select room type', max_length=20),
        ),
    ]
