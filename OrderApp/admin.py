from django.contrib import admin
from OrderApp.models import ShopCart, Order, OrderProduct

# Register your models here.


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount']
    list_filter = ['user']


class OrderProductlines(admin.TabularInline):
   model = OrderProduct
   readonly_fields = ('user', 'product', 'quantity', 'price', 'amount')
   can_delete = False
   extra = 0



admin.site.register(ShopCart,ShopCartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'phone', 'total', 'status', 'transaction_id']
    list_filter = ['status']
    readonly_fields = ('user', 'first_name', 'last_name',
                       'phone', 'address', 'city', 'country', 'total', 'ip', 'transaction_id', 'image_tag')
    can_delete = False
    inlines = [OrderProductlines] 
   


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']

admin.site.register(Order, OrderAdmin) #, OrderAdmin
admin.site.register(OrderProduct, OrderProductAdmin) #OrderProductAdmin