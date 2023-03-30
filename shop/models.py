from django.db import models

class Product(models.Model):
    category = models.IntegerField()
    name = models.CharField(max_length= 200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    img = models.ImageField(upload_to="images/" , blank=True)
        
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.IntegerField()
    name = models.CharField(max_length= 200)
    img = models.ImageField(upload_to="images/" , blank=True)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
