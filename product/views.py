from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='accounts:login')
def detail(request):
    context={}
    return render(request,'product/detail.html',context)
@login_required(login_url='accounts:login')
def shop(request):
    product=Product.objects.order_by('?').all()
    category=Category.objects.all()
    
    context={'product':product,'category':category,}
    return render(request,'product/shop.html',context)

