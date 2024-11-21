from django.shortcuts import render,redirect
from.models import Order,OrderedItem
from product.models import Product
from customer.models import Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_cart(request):
    user=request.user
    customer = user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
    context={'cart':cart_obj}
    
    return render(request,'cart.html',context)

@login_required(login_url='show_account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Product.objects.get(pk=product_id)
        orderd_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj
  
        )
        if created:
            orderd_item.quantity=quantity
            orderd_item.save()
        else:
           orderd_item.quantity=orderd_item.quantity+quantity
           orderd_item.save()
            
        return redirect('show_cart')
def remove_item(request,id):
        item=OrderedItem.objects.get(id=id)
        if item:
            item.delete()
        return redirect('show_cart')
def checkout_cart(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message="your order is confirmed"
                messages.success(request,status_message)
            else:
                error_message="failed"
                messages.error(request,error_message)
        except Exception as e:
                error_message="failed"
                messages.error(request,error_message)
    return redirect('show_cart')   
@login_required(login_url='show_account')
def view_orders(request):
    user=request.user
    customer = user.customer_profile
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
    return render(request,'orders.html',context)

# def payment(request):
#     return render(request,'payment.html')    


# @csrf_exempt
# def sucess(request):
#     return render(request,'succcess.html')
   


   
            