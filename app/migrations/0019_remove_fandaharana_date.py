# Generated by Django 4.1.1 on 2022-10-30 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_fandaharana'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fandaharana',
            name='date',
        ),
    ]