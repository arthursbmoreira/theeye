# Generated by Django 3.2.9 on 2021-11-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theeyeservice', '0002_auto_20211113_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payload',
            name='element',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
