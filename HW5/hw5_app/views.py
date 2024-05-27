from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product, Order
from .forms import ProductForm

def index(request):
    return render(request, 'hw5_app/index.html')


def client_order(request, client_id):
    client = Client.objects.get(pk=client_id)

    orders_last_7_days = client.order_set.filter(order_date__gte=timezone.now() - timedelta(days=7))
    orders_last_30_days = client.order_set.filter(order_date__gte=timezone.now() - timedelta(days=30))
    orders_last_365_days = client.order_set.filter(order_date__gte=timezone.now() - timedelta(days=365))
    
    all_products = Product.objects.all()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save()
            
            return redirect('client_order', client_id=client.id)
    else:
        product_form = ProductForm()

    context = {
        'client': client,
        'orders_last_7_days': orders_last_7_days,
        'orders_last_30_days': orders_last_30_days,
        'orders_last_365_days': orders_last_365_days,
        'all_products': all_products,
        'product_form': product_form,
    }

    return render(request, 'hw5_app/client_order.html', context)
