# Generated by Django 4.1.1 on 2022-10-28 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_delete_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.IntegerField()),
                ('password', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
