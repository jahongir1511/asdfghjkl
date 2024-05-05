from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = 'category'

    def __str__(self) -> str:
        return self.name


class products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    body = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/products', blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self) -> str:
        return f"{self.category.name}, {self.model}"


class Products:
    pass