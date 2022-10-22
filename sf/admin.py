from django.contrib import admin

# Register your models here..
from.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =('id', 'first_name','last_name','username', 'email', 'password','confirm_password','profile_picture','category')

# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
#     list_display =('id', 'address','state','name', 'city', 'zipcode','country')