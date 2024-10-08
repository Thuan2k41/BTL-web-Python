from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            # Kiểm tra xem tên người dùng đã tồn tại chưa
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
            else:
                form.save()
                messages.success(request, 'Registration successful!')
                return redirect('login')  # Redirect to login page after successful registration
        else:
            # Thêm thông báo lỗi cho các trường không hợp lệ
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.error(request, f"{field.capitalize()}: {error}")

    context = {'form': form}
    return render(request, 'app/register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        #if username and password:   Kiểm tra username và password không rỗng
        user = authenticate(request, username =username, password =password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password not correct!')
    context = {}
    return render(request, 'app/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login')
def home(request):
    products = Product.objects.all() #tror tới class Product
    context={'products':products}
    return render(request,'app/base.html',context)
def cart(request):
    context={}
    return render(request,'app/cart.html',context)
# def checkout(request):
#     context={}
#     return render(request,'app/checkout.html',context)