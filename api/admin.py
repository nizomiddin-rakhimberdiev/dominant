from django.contrib import admin

from .models import Service, Order, Review


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'service', 'service_id', 'phone', 'order_status')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'star')

admin.site.register(Service)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)

