from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug= models.SlugField(max_length=200,blank=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

class Variant(models.Model):
    color = models.CharField(max_length=50)
    Size = models.IntegerField(max_length=50)

    def __str__(self):
        return self.color

class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    color = models.ForeignKey(Variant, blank=True, null=True, on_delete=models.PROTECT)
    pro_name= models.CharField(max_length=50)
    image= models.ImageField(upload_to='static/products')
    price= models.DecimalField(max_digits=10,decimal_places=2)
    description= models.TextField()
    stock= models.IntegerField()

    def __str__(self):
        return self.pro_name
    

    # slug= models.SlugField(max_length=200,blank=True)
     




                                     
