from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from cart.models import *
from cart.forms import *
# Create your views here.
@login_required(login_url='accounts:login')
def home(request):
    product=Product.objects.all().order_by('?')[:3]
    latest_product=Product.objects.order_by('-id')[:4]
    picked_product=Product.objects.all().order_by('?')[:4]
    context={'product':product,'latest_product':latest_product,'picked_product':picked_product}
    
    return render(request,'boutique/home.html',context)


def product_detail(request,id,slug):
    product=Product.objects.get(pk=id)
    detail=Product.objects.get(pk=id)
    image=Images.objects.filter(product_id=id)
    comment=Comment.objects.filter(product_id=id)
    related_product=Product.objects.filter(category_id=product.category_id).exclude(pk=product.id).order_by('?')[:4]
    context={'detail':detail,'image':image,'related_product':related_product,'product':product,'comment':comment}
    return render(request,'boutique/product_detail.html',context)

def category_product(request,id,slug):
     category_product=Product.objects.filter(category_id=id)
     context={'category_product':category_product}
     return render(request,'boutique/category_product.html',context)

def addComment(request,id):
   
    url=request.META.get('HTTP_REFERER')
    current_user=request.user
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            data=Comment()
            data.subject=form.cleaned_data.get('subject')
            data.comment=form.cleaned_data.get('comment')
            data.user_id=current_user.id
            data.product_id=id
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Comment added successfully')
            return HttpResponseRedirect(url)


    return HttpResponseRedirect(url)

def about(request):
    setting=Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request,'boutique/aboutus.html',context)

def addtoshopcart(request,id):
    url=request.META.get('HTTP_REFERER')
    current_user=request.user
    product=Product.objects.get(pk=id)
    checkproduct=ShopCart.objects.filter(user_id=current_user.id,product_id=id)
    if checkproduct:
        control=1
    else:
        control=0
    if request.method=='POST':
        form =ShopCartForm(request.POST)
        if form.is_valid():
            if control==1:
                data=ShopCart.objects.get(product_id=id,user_id=current_user.id)
                
                data.quantity += form.cleaned_data.get('quantity')
                data.save()
            else:
                data=ShopCart()
                data.user_id=current_user.id
                data.product_id=id
                data.quantity = form.cleaned_data.get('quantity')
                data.save()
            messages.success(request,'product added to cart successfully')
            return HttpResponseRedirect(url)
    else:
        if control==1:
            data=ShopCart.objects.get(product_id=id,user_id=current_user.id)
            
            data.quantity += 1
            data.save()
        else:
            data=ShopCart()
            data.user_id=current_user.id
            data.product_id=id
            data.quantity = 1
            data.save()
        messages.success(request,'product added to cart successfully')
        return HttpResponseRedirect(url)
   
