from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Catagories'
        
    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    catagory = models.ForeignKey(Catagory,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255,blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Items'
        
    def __str__(self):
        return self.name,self.catagory
        
    