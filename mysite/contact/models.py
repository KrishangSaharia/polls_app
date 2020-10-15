from django.db import models


class Details(models.Model):
    date=models.DateTimeField()
    name=models.CharField(max_length=100)
    number=models.IntegerField()
    mail_id=models.CharField(max_length=100)
# Create your models here.
