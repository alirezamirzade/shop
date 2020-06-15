from django.db import models
from .product import Product
from .customer import Customer
import datetime
from extensions.utils import jalali_converter

class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,verbose_name="کالا")
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,verbose_name="کاربر")
    quantity = models.IntegerField(default=1,verbose_name="تعداد")
    price = models.IntegerField(verbose_name="قیمت")
    address = models.CharField(max_length=50, default='', blank=True,verbose_name="آدرس")
    phone = models.CharField(max_length=50, default='', blank=True,verbose_name="شماره تلفن")
    date = models.DateField(default=datetime.datetime.today,verbose_name="تاریخ")
    status = models.BooleanField(default=False,verbose_name="وضعیت")

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural ="سفارش ها"

    def jdate(self):
        return jalali_converter(self.date)