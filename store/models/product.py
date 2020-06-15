from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50,verbose_name="نام")
    price = models.IntegerField(default=0,verbose_name="قیمت")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1,verbose_name="دسته")
    description = models.CharField(max_length=200, default='' , null=True , blank=True,verbose_name="توصیف")
    image = models.ImageField(upload_to='uploads/products/',verbose_name="عکس")

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "کالا"
        verbose_name_plural ="کالا ها"
    