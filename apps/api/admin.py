from django.contrib import admin

from .models import Service, Order, Review, News, Candidate, Consultation, Category, CategoryService


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'action_price')


class CategoryServiceAdmin(admin.ModelAdmin):
    def service_price(self, obj):
        return f"{obj.service.price} -  {obj.service.action_price}"

    list_display = ('id', 'service', 'service_price', 'category', 'created_at')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'service_id', 'phone', 'order_status')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'star')


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone', 'resume', 'service')


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'phone', 'status', 'created_at')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryService, CategoryServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)

admin.site.register(News)

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Consultation, ConsultationAdmin)
