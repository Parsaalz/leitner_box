from django.db import models
from django.contrib.auth.models import User
class LitnerApp(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    level=models.SmallIntegerField(default=0)
    dl=models.DateField()
    word=models.CharField(max_length=100)
    answer=models.CharField(max_length=100,blank=True,null=True)
    show=models.BooleanField(default=True)

    class Meta:
        verbose_name="لایتر اپ"
        verbose_name_plural="لایتنر اپ"

    def __str__(self):
        return f"{self.word} {self.user}"


class PremiumAccount(models.Model):
    title=models.CharField(max_length=100,verbose_name="عنوان")
    description=models.TextField(verbose_name="توضیحات")
    price=models.IntegerField(verbose_name="قیمت")
    time=models.IntegerField(verbose_name="زمان استفاده")
    

    class Meta:
        verbose_name="اکانت پرمیوم"
        verbose_name_plural="اکانت های پرمیوم"

    def __str__(self):
        return self.title


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    payment_date=models.DateTimeField(null=True,blank=True,verbose_name="تاریخ پرداخت")
    is_paid=models.BooleanField(default=False,verbose_name="انجام شده/ نشده")
    is_delete=models.BooleanField(default=False,verbose_name="منقضی شده")

    class Meta:
        verbose_name="سفارش"
        verbose_name_plural="سفارش ها"


    def __str__(self):
        return str(self.user)

class OrderDetail(models.Model):
    premium=models.ForeignKey(PremiumAccount,on_delete=models.CASCADE,verbose_name="نوع پرمیوم")
    order=models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="سفارش")
    final_price=models.IntegerField(null=True,blank=True,verbose_name="قیمت")


    class Meta:
        verbose_name="جزییات سفارش"
        verbose_name_plural="جزییات سفارش ها"


    def __str__(self):
        return str(self.order)


