from django.contrib import admin
from .models import user_register

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number')

admin.site.register(user_register, UserAdmin)