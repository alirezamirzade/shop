from django.db import  models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    first_name = models.CharField(max_length=50,verbose_name="نام")
    last_name = models.CharField(max_length=50,verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=15,verbose_name="شماره تلفن")
    email = models.EmailField(verbose_name="ایمیل")
    password = models.CharField(max_length=500,verbose_name="رمز عبور")

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural ="کاربرها"

