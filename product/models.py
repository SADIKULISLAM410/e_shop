from django.db import models
from django.utils.safestring import mark_safe
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    
    parents = models.ForeignKey('self',blank=True, null=True, related_name='chilren', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    images = models.ImageField(upload_to ='images/',blank=True)
    status = models.CharField(max_length=50, choices=STATUS)
    slug = AutoSlugField(populate_from='title')
    # stock = models.IntegerField()
    # is_available = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    # update_date = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(upload_to='images/',blank=True)
    status = models.CharField(max_length=50, choices=STATUS)
    detail=RichTextField()
    price = models.FloatField()
    amount=models.IntegerField()
    stock = models.IntegerField()
    slug = AutoSlugField(populate_from='title')
    min_amount=models.IntegerField(default=3)
    is_available = models.BooleanField(default=True)
    create_date =models.DateTimeField(auto_now_add=True)
    update_date =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        #if self.image.url is not None:
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        # else:
        #     return ""
        image_tag.short_description = 'Image'

class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.title
    