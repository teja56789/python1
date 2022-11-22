from django.db import models
import uuid

# Create your models here.

from django.db import models



class Item(models.Model):
    name = models.CharField(max_length = 50 , null = False)
    description = models.CharField(max_length = 200 , null = True)
    price = models.IntegerField(null=False)
    # discount = models.IntegerField(null=False , default = 0) 
    active = models.BooleanField(default = False)
    thumbnail = models.ImageField(upload_to = "images/") 
    created=models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    

    def __str__(self):
        return self.name



class offer(models.Model):
    code = models.CharField(max_length=10)
    Item=models.ForeignKey(Item, on_delete=models.CASCADE, related_name ='offer')
    discount = models.IntegerField(default=0)
    created=models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    
    def __str__(self):
        return self.code