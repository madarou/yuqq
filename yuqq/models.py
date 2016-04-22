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
    show=models.CharField(max_length=3,null=True)
    
class Index(BaseModel):
    name=models.CharField(max_length=30,null=True)
    price=models.CharField(max_length=8,null=True)
    slogan=models.CharField(max_length=50,null=True)
    pic=models.CharField(max_length=40,null=True)
    type=models.CharField(max_length=20,null=True)
    
class Order(BaseModel):
    product_name=models.CharField(max_length=30,null=True)
    product_num=models.CharField(max_length=5,null=True)
    product_price=models.CharField(max_length=8,null=True)
    total_cost=models.CharField(max_length=10,null=True)
    user_remark=models.CharField(max_length=80,null=True)
    send_home=models.CharField(max_length=3,null=True)
    user_name=models.CharField(max_length=20,null=True)
    fetch_date=models.CharField(max_length=20,null=True)
    contact=models.CharField(max_length=30,null=True)
    send_date=models.CharField(max_length=20,null=True)
    send_address=models.CharField(max_length=50,null=True)
    order_date=models.DateTimeField(null=True)
    actual_cost=models.CharField(max_length=10,null=True)
    yqq_remark=models.CharField(max_length=80,null=True)
    
class Service(BaseModel):
    type=models.CharField(max_length=10,null=True)
    user_name=models.CharField(max_length=20,null=True)
    service_date=models.CharField(max_length=20,null=True)
    contact=models.CharField(max_length=30,null=True)
    address=models.CharField(max_length=50,null=True)
    user_remark=models.CharField(max_length=80,null=True)
    yqq_remark=models.CharField(max_length=80,null=True)
    order_date=models.DateTimeField(null=True)
    actual_cost=models.CharField(max_length=10,null=True)
    
class Faq(BaseModel):
    question=models.CharField(max_length=255,null=True)
    answer=models.CharField(max_length=255,null=True)
    ask_time=models.DateTimeField(null=True)
    answer_time=models.DateTimeField(null=True)

class Message(BaseModel):
    user_name=models.CharField(max_length=20,null=True)
    contact=models.CharField(max_length=30,null=True)
    content=models.CharField(max_length=255,null=True)
    time=models.DateTimeField(null=True)

class Visitor(BaseModel):
    ip=models.CharField(max_length=20,null=True)
    time=models.DateTimeField(null=True)
    
class News(BaseModel):
    title=models.CharField(max_length=255,null=True)
    answer=models.CharField(max_length=255,null=True)
    time=models.DateTimeField(null=True)
    popularit=models.CharField(max_length=10,null=True)
    
class Tips(BaseModel):
    title=models.CharField(max_length=255,null=True)
    content=models.TextField(null=True)
    time=models.DateTimeField(null=True)
    popularit=models.CharField(max_length=10,null=True)
    
if __name__=="__main__":
    #from yuqq.models import Product
    intro = Introduction(name="hello")
    intro.save()
    product = Product(name="血色鹦鹉",price_low="200",slogan="发财鱼",catalogue="水生生物",inventory="30",remarks="还剩最后2只")
    product = Product(name="锦鲤",price_low="130",slogan="吉祥如意，年年有余",catalogue="水生生物",inventory="30",remarks="春节促销中")
    product = Product(name="宝莲灯",price_low="20",slogan="照亮前程",catalogue="水生生物",inventory="30",remarks="还剩最后20只")
    product = Product(name="大白微生态系统",price_low="180",slogan="让自然回到身边",catalogue="水族设备",inventory="30")
    product.save()