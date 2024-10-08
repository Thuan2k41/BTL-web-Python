from django.contrib import admin
from .models import *
# Register your models here.
#ddanwg kis những class đã tạo trong models.py
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)