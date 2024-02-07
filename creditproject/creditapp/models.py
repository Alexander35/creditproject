from django.db import models

class CreditOrder(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Contract(models.Model):
    name = models.CharField(max_length=50)
    credit_order = models.OneToOneField(
        CreditOrder,
        on_delete=models.CASCADE,
        related_name='contract'
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=50)
    credit_order = models.ForeignKey(
        CreditOrder,
        on_delete=models.CASCADE,
        related_name='products'
    )
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='products'
    )
    created_at = models.DateTimeField(auto_now_add=True)