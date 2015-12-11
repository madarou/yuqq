#coding=utf-8
from django.db import models
#from django.core import serializers
import datetime
import json
class BaseModel(models.Model):
    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
    
        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr),datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr),datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            elif isinstance(getattr(self, attr),models.Model):
                #d[attr] = serializers.serialize("json", [getattr(self, attr)])跳过外键关联的Model的序列化
                pass
            else:
                d[attr] = getattr(self, attr)
          
        return json.dumps(d)
    class Meta:
            abstract = True
            
# Create your models here.
class Introduction(BaseModel):
    name=models.CharField(max_length=30,null=True)
    brief_intro=models.CharField(max_length=255,null=True)
    raise_method=models.CharField(max_length=255,null=True)
    use_method=models.CharField(max_length=255,null=True)
    remarks=models.CharField(max_length=255,null=True)
    pic1=models.CharField(max_length=40,null=True)
    pic2=models.CharField(max_length=40,null=True)
    type=models.CharField(max_length=10,null=True)

class Product(BaseModel):
    name=models.CharField(max_length=30,null=True)
    price_low=models.CharField(max_length=8,null=True)
    price_high=models.CharField(max_length=8,null=True)
    slogan=models.CharField(max_length=50,null=True)
    introduction=models.OneToOneField(Introduction,null=True)
    catalogue=models.CharField(max_length=10,null=True)
    inventory=models.CharField(max_length=5,null=True)
    time_to_market=models.DateField(null=True)
    pic1=models.CharField(max_length=40,null=True)
    pic2=models.CharField(max_length=40,null=True)
    pic3=models.CharField(max_length=40,null=True)
    pic4=models.CharField(max_length=40,null=True)
    pic5=models.CharField(max_length=40,null=True)
    related1=models.CharField(max_length=30,null=True)
    related2=models.CharField(max_length=30,null=True)
    related3=models.CharField(max_length=30,null=True)
    related4=models.CharField(max_length=30,null=True)
    popularity=models.CharField(max_length=50,null=True)
    remarks=models.CharField(max_length=50,null=True)
    kind=models.CharField(max_length=20,null=True)
if __name__=="__main__":
    #from yuqq.models import Product
    intro = Introduction(name="hello")
    intro.save()
    product = Product(name="血色鹦鹉",price_low="200",slogan="发财鱼",catalogue="水生生物",inventory="30",remarks="还剩最后2只")
    product = Product(name="锦鲤",price_low="130",slogan="吉祥如意，年年有余",catalogue="水生生物",inventory="30",remarks="春节促销中")
    product = Product(name="宝莲灯",price_low="20",slogan="照亮前程",catalogue="水生生物",inventory="30",remarks="还剩最后20只")
    product = Product(name="大白微生态系统",price_low="180",slogan="让自然回到身边",catalogue="水族设备",inventory="30")
    product.save()