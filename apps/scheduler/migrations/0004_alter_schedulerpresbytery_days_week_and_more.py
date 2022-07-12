# Generated by Django 4.0.6 on 2022-07-12 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_daysweekpresbytery_hoursdayspresbytery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulerpresbytery',
            name='days_week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scheduler.daysweekpresbytery'),
        ),
        migrations.AlterField(
            model_name='schedulerpresbytery',
            name='hours_days',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scheduler.hoursdayspresbytery'),
        ),
    ]
