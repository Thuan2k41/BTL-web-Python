from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False) #null = True sẽ lưu gias trị rỗng,blank k được bỏ trống ô điền User 
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
     
    def __str__(self):
        return self.name

class Product(models.Model):
    #user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False) #null = True sẽ lưu gias trị rỗng,blank k được bỏ trống ô điền User 
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)
    image = models.ImageField(null=True,blank=True)
    #chefn anhr vào 
    def __str__(self):
        return self.name
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)#foreign key laays tên dữ liệu trên trường Customer 
    date_order = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200,null=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    def __str__(self):
        return str(self.id)