from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

class AdminUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(is_superuser=True, is_staff=True)

class ClientUserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(is_superuser=False, is_staff=False)

class AdminUser(NewUser):
    objects = AdminUserManager()

    class Meta:
        proxy = True
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'

class ClientUser(NewUser):
    objects = ClientUserManager()
    class Meta:
        proxy = True
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

@admin.register(AdminUser)
class AdminUserAdmin(UserAdmin):
    # Customize the display fields for Admin users
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_verified', 'is_premium', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_staff', 'is_superuser', 'is_verified', 'is_premium', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

@admin.register(ClientUser)
class ClientUserAdmin(UserAdmin):
    # Customize the display fields for Client users
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_verified', 'is_premium', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)

@admin.register(NewUser)
class UserAdmin(admin.ModelAdmin):
    # Common configuration for both Admins and Clients
    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'is_verified', 'is_premium', 'is_logged_in', 'is_deleted', 'is_active', 'created_at', 'updated_at')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')

    filter_horizontal = ()
    list_filter = (
        'is_staff', 'is_superuser', 'is_active', 'is_logged_in', 'is_verified', 'is_premium', 'is_deleted'
    )
    fieldsets = (
        (None, 
            {'fields': 
                ('email', 'password', 'username', 'first_name', 'last_name',)
            }
        ),
        ('Roles', 
            {'fields': 
                ('is_staff', 'is_superuser')
            }
        ),
        ('Status', 
            {'fields': 
                ('is_active', 'is_logged_in', 'is_verified', 'is_premium', 'is_deleted')
            }
        ),
        ('Timestamps', 
            {'fields': 
                ('created_at', 'updated_at')
            }
        ),
    )

