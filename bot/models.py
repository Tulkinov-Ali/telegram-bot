from django.db import models


class Tg_user(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128, null=True)
    surname = models.CharField(max_length=128, null=True)
    username = models.CharField(max_length=64)
    phone = models.CharField(max_length=20, null=True)
    lang = models.CharField(max_length=2, default='en')
    log = models.JSONField(default={'state': 0})
    is_admin = models.BooleanField(default=False)
    menu = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=128)
    img = models.ImageField(upload_to='ctg')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=128)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='products')
    price = models.IntegerField()
    desc = models.TextField()


class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user_id = models.BigIntegerField()
    quant = models.IntegerField(default=1)
    summ = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.summ = int(self.quant) * int(self.product.price)
        return super(Cart, self).save(*args, **kwargs)
