# Generated by Django 4.1.1 on 2022-10-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_asa_date_asa_title_alter_rafitra_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fampianarana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('sudo', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
    ]
