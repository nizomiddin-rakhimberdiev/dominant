from django.contrib import admin
<<<<<<< HEAD:users/admin.py
from django import forms
# from phonenumber_field.widgets import PhoneNumberPrefixWidget
=======
from phonenumber_field.widgets import PhoneNumberPrefixWidget
>>>>>>> 6fe8416 (complated):apps/users/admin.py

from apps.users.models import CustomUser


# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'first_name', 'last_name')


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'phone_number':
            kwargs['widget'] = PhoneNumberPrefixWidget
        return super(UserAdmin, self).formfield_for_dbfield(db_field, **kwargs)


# admin.site.register(CustomUser, UserAdmin, CustomUserAdmin)
