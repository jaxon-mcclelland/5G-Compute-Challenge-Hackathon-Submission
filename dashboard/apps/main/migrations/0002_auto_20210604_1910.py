# Generated by Django 3.2.4 on 2021-06-05 02:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='iotdevice',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iotdevice',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
