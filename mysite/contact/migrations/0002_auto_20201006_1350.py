# Generated by Django 3.1.2 on 2020-10-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='number',
            field=models.IntegerField(),
        ),
    ]