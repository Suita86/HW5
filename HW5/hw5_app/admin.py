from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'address', 'registration_date')
    search_fields = ('name', 'email')
    list_filter = ('order__products', 'order__order_date')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'quantity', 'added_date')
    search_fields = ('name', 'description')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')
    search_fields = ('client__name', 'id')
    filter_horizontal = ('products',)
    

admin.site.register(Product,ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
