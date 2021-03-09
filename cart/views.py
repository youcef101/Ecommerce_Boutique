from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from accounts.models import *
from django.utils.crypto import get_random_string
from django.contrib import messages
# Create your views here.

@login_required(login_url='accounts:login')
def shopcart(request):
    current_user=request.user
    shopcart=ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for item in shopcart:
        total += item.amount #or we can get total with " total += item.product.price * item.quantity "
    context={'shopcart':shopcart,'total':total}
    return render(request,'cart/cart.html',context)

def delete_shopcart_item(request,id):
    url=request.META.get('HTTP_REFERER')
    shopcart=ShopCart.objects.get(pk=id)
    shopcart.delete()
    return HttpResponseRedirect(url) 

@login_required(login_url='accounts:login')
def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for item in shopcart:
        total += item.product.price * item.quantity
      

    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        #return HttpResponse(request.POST.items())
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
            # ..............

            data = Order()
            data.first_name = form.cleaned_data['first_name'] #get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.country = form.cleaned_data['country']
            data.phone = form.cleaned_data['phone']
            data.zipcode = form.cleaned_data['zipcode']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode= get_random_string(5).upper() # random cod
            data.code =  ordercode
            data.save() #


            for item in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id # Order Id
                detail.product_id = item.product_id
                detail.user_id = current_user.id
                detail.quantity = item.quantity
                detail.price = item.product.price
                detail.amount = item.amount
                detail.save()
                # ***Reduce quantity of sold product from Amount of Product
                
                product = Product.objects.get(id=item.product_id)
                product.amount -= item.quantity
                product.save()
               
                #************ <> *****************

            ShopCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
            request.session['cart_items']=0
            messages.success(request, "Your Order has been completed. Thank you ")
            context={'ordercode':ordercode,'category': category}
            return render(request, 'cart/order_completed.html',context)
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect(reverse("paiyement:orderproduct"))

    form= OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'cart/checkout.html', context)