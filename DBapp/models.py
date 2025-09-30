from django.db import models

# Create your models here





class Address(models.Model):
    house_no=models.CharField(max_length=15)
    street_name=models.CharField(max_length=15)
    area_name=models.CharField(max_length=25)
    city=models.CharField(max_length=25)

    def __str__(self):
        return f"{self.house_no}, {self.street_name}, {self.area_name}, {self.city}"

class Owner(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=254)
    address=models.OneToOneField(Address,null=True,on_delete=models.CASCADE,related_name='addr')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.mobile} ,{self.email})"





class Flat(models.Model):
    block_name=models.CharField(max_length=100)
    flat_num=models.IntegerField()
    status=models.BooleanField(default=False)
    br_count=models.SmallIntegerField(null=True)
    owner=models.ForeignKey(Owner,null=True,on_delete=models.CASCADE,related_name='flats')

    def __str__(self):
        return f"{self.block_name} - {self.flat_num}"