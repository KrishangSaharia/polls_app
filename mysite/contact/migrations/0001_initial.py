# Generated by Django 3.1.2 on 2020-10-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(max_length=50)),
                ('mail_id', models.CharField(max_length=100)),
            ],
        ),
    ]