from django.db import models
from django.utils import timezone
class Dealer(models.Model):
    dealer_name= models.CharField(max_length=100)



class Sale(models.Model):
    date= timezone.now()
    transaction=models.IntegerField(default=0)
    dealer = models.ForeignKey(Dealer , on_delete = models.CASCADE)
class Purchase(models.Model):
    date= timezone.now()
    transaction=models.ForeignKey(Dealer, on_delete=models.CASCADE)




# Create your models here.
