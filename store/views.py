from django.shortcuts import render,redirect
from .models import Product, Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


def category(request, type):
  #replace hypens with space
  type = type.replace('-',' ')
  #grab the category from the url 
  try:
    #look up the category 
    category = Category.objects.get(name=type)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html',{'products':products,'category':category,})
  except:
    messages.success(request,("That category doesn't exit.."))
    return redirect('home')

def product(request,pk):
   product = Product.objects.get(id=pk)
   return render(request,'product.html',{'product':product})

def home(request):
  products = Product.objects.all()
  return render(request,'home.html',{'products':products})

def about(request):
  return render(request,'about.html',{})

def login_user(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      messages.success(request,("You have been logged in successfully!"))
      return redirect('home')
    else:
      messages.success(request,("There was an error while logging in..."))
      return render(request,'login.html',{})
    
  else:
    return render(request,'login.html',{})
    

def logout_user(request):
  logout(request)
  messages.success(request,("You have been logged out.Thanks for stopping by....."))
  return redirect('home')

def  register_user(request):
  form = SignUpForm()
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
                                    
      #loginuser
      # user = authenticate(username=username, password=password)
      user = form.save()
      login(request,user)
      messages.success(request,("You have registered successfully."))
      return redirect('home')
    else:
      messages.success(request,('Whoops!There was a problem while attempting registering...'))
      return redirect('register_user')

  else:
    return render(request,'register.html',{'form':form})