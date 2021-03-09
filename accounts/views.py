from django.shortcuts import render
from .forms import*
from .models import UserProfile
from django.contrib.auth.models import Group,User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse
from .decorators import notLoggedUser
from boutique.models import Comment
from cart.models import *

# Create your views here.
@notLoggedUser
def register(request):
    url=request.META.get('HTTP_REFERER')
    if request.method=='POST':
        form=createNewUser(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name="customer")
            users=user.groups.add(group)
            instance=User.objects.get(username=username)
            UserProfile.objects.create(user=instance)
            messages.success(request,username +' Successfully created')
            return HttpResponseRedirect(url)
           
    context={}
    return render(request,'auth/register.html',context)
@notLoggedUser
def userLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('home:home'))
            messages.success(request,' Hello'+username)
        else:
            messages.warning(request,'password and username dont match')
    context={}
    return render(request,'auth/login.html',context)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

def user_profile(request):
    current_user=request.user
    profile=UserProfile.objects.get(user_id=current_user.id)
    context={'profile':profile}
    return render(request,'auth/user_profile.html',context)
def update_profile(request):
    current_user=request.user
    profile=UserProfile.objects.get(user_id=current_user)
    if request.method=='POST':
        form_profile=updateProfile(request.POST,request.FILES,instance=profile)
        form_user=updateUserProfile(request.POST,instance=current_user)
        if form_profile.is_valid() and form_user.is_valid():
            form_profile.save()
            form_user.save()
            messages.success(request,'Account updated successfully')
            return HttpResponseRedirect(reverse('accounts:profile'))
    else:
        form_profile=updateProfile(instance=profile)
        form_user=updateUserProfile(instance=current_user)
    context={
         'form_profile':form_profile,
         'form_user':form_user}
    return render(request,'auth/update_profile.html',context)

def user_comment(request):
    current_user=request.user
    comment=Comment.objects.filter(user_id=current_user.id)
    context={'comment':comment}
    return render(request,'auth/user_comments.html',context)

def delete_comment(request,id):
    url=request.META.get('HTTP_REFERER')
    comment=Comment.objects.filter(pk=id).delete()
    return HttpResponseRedirect(url)

def user_orders(request):
    current_user=request.user
    orders=Order.objects.filter(user_id=current_user.id)
    context={'orders':orders}
    return render(request,'auth/user_orders.html',context)

def user_orders_detail(request,id):
    
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, pk=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {
        
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, 'auth/user_orders_detail.html', context)

def user_orders_product(request):
    
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id).order_by('-id')
    context = {
               'order_product': order_product,
               }
    return render(request, 'auth/user_order_products.html', context)


def user_orders_product_detail(request,id,oid):
   
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=oid)
    orderitems = OrderProduct.objects.filter(pk=id,user_id=current_user.id)
    context = {
        
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, 'auth/user_orders_detail.html', context)