
# Create your models here.
from django.db import models

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    send_method = models.CharField(max_length=255)
    receive_method = models.CharField(max_length=255)
    send_data = models.CharField(max_length=255)
    receive_date = models.CharField(max_length=255)
    price = models.CharField(max_length=255)


class Package(models.Model):
    id = models.IntegerField(primary_key=True)
    package_type = models.CharField(max_length=250)
    weight = models.FloatField(max_length=250)
    contents = models.CharField(max_length=250)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)


class Sender(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)


class Receiver(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    place_of_prod = models.CharField(max_length=250)
    price = models.FloatField(max_length=250)
    country = models.CharField(max_length=250)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)


class Payment(models.Model):
    id = models.IntegerField(primary_key=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    choice = models.CharField(max_length=255)