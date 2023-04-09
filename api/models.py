from django.db import models

# Create your models here.
class  Product(models.Model):
    title=models.CharField(max_length=10)
    price=models.PositiveSmallIntegerField(default=0,null=True,blank=True)
    discount=models.DecimalField(max_digits=14,decimal_places=2,default=9.02)

    def __str__(self):
        return self.title
    
    def get_discount(self):
        return self.price*(self.discount/100)
    
    