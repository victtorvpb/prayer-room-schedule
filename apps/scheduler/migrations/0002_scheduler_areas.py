# Generated by Django 4.0.6 on 2022-07-10 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduler',
            name='areas',
            field=models.CharField(default='', max_length=20),
        ),
    ]