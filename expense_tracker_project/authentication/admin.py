from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_staff','is_superuser',]
    search_fields = ['email']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','is_staff'),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, CustomUserAdmin)

