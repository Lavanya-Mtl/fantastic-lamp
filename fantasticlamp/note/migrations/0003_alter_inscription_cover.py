# Generated by Django 3.2.4 on 2021-07-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20210630_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='cover',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
