from django.contrib import admin

from .models import Service, Order


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'service_id', 'phone', 'order_status')


admin.site.register(Service)
admin.site.register(Order, OrderAdmin)
